from app.core.request_objects.user import UserAuthenticateRequestObject


def test_build_user_authenticate_request_object_from_empty_dict():
    result = UserAuthenticateRequestObject.from_dict({})

    assert bool(result) == False


def test_build_user_authenticate_request_object_from_valid_dict():
    USER_EMAIL = "test@test.com"
    USER_PASSWORD = "super-secret"

    result = UserAuthenticateRequestObject.from_dict({
        "email": USER_EMAIL,
        "password": USER_PASSWORD,
    })

    assert bool(result) is True
    assert result.email == USER_EMAIL
    assert result.password == USER_PASSWORD
