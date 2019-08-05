from app.core.request_objects.user_auth_request_object import UserAuthRequestObject


def test_build_user_authenticate_request_object_from_empty_dict():
    result = UserAuthRequestObject.from_dict({})

    assert bool(result) == False


def test_build_user_authenticate_request_object_from_valid_dict():
    USER_EMAIL = "test@test.com"
    USER_PASSWORD = "super-secret"

    result = UserAuthRequestObject.from_dict(
        {"email": USER_EMAIL, "password": USER_PASSWORD}
    )

    assert bool(result) is True
    assert result.email == USER_EMAIL
    assert result.password == USER_PASSWORD
