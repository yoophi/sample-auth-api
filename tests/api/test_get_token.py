import json
from unittest import mock

from flask import url_for

from app.core.domain import User

domain_user = User.from_dict({"id": 1, "email": "test@gmail.com", "password": "secret"})


@mock.patch("app.adaptors.UserAdaptor")
def test_get_access_token(mock_user_adaptor, client):
    mock_user_adaptor().authenticate.return_value = domain_user

    http_response = client.post(
        url_for("auth.access_token"),
        data=(json.dumps({"email": "test@test.com", "password": "secret"})),
        content_type="application/json",
    )
    assert http_response.status_code == 200


@mock.patch("app.adaptors.UserAdaptor")
def test_get_access_token_with_invalid_grant(mock_user_adaptor, client):
    mock_user_adaptor().authenticate.return_value = None

    http_response = client.post(
        url_for("auth.access_token"),
        data=(json.dumps({"email": "test@test.com", "password": "secret"})),
        content_type="application/json",
    )
    assert http_response.status_code == 401


@mock.patch("app.adaptors.UserAdaptor")
def test_get_and_validate_token(mock_user_adaptor, client):
    mock_user_adaptor().authenticate.return_value = domain_user

    http_response = client.post(
        url_for("auth.access_token"),
        data=(json.dumps({"email": "test@test.com", "password": "secret"})),
        content_type="application/json",
    )
    assert http_response.status_code == 200

    access_token = http_response.json["access_token"]
    validation_response = client.get(
        url_for("auth.validate_token"),
        headers={"Authorization": f"Bearer {access_token}"},
    )

    assert validation_response.status_code == 200
    assert validation_response.json["user_id"] == domain_user.id


def test_validate_token_with_invalid_access_token(client):
    INVALID_ACCESS_TOKEN = "INVALID.ACCESS.TOKEN"
    http_response = client.get(
        url_for("auth.validate_token"),
        headers={"Authorization": f"Bearer {INVALID_ACCESS_TOKEN}"},
    )
    assert http_response.status_code == 422

    EXPIRED_ACCESS_TOKEN = (
        "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjQ5ODA2MzgsIm5iZiI6MTU2NDk4MDYzOCwianRpIjoiZTg"
        "yNTMzZWQtMjJmOS00Yzg1LWEwZTktNzY4OGY5YmI4MTZiIiwiZXhwIjoxNTY0OTgxNTM4LCJpZGVudGl0eSI6InRlc3QiLCJ"
        "mcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.o6mtBG0HOR7-xRi81TJaf4g--KXaodaIUYz7u52eR8s"
    )

    http_response = client.get(
        url_for("auth.validate_token"),
        headers={"Authorization": f"Bearer {EXPIRED_ACCESS_TOKEN}"},
    )
    assert http_response.status_code == 401
