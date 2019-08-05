from app.core.domain import User


def test_user_model_init():
    USER_ID = 1
    USER_EMAIL = "test@test.com"
    USER_PASSWORD = "secret"

    user = User(id=USER_ID, email=USER_EMAIL, password=USER_PASSWORD)

    assert user.id == USER_ID
    assert user.email == USER_EMAIL
    assert user.password == USER_PASSWORD


def test_user_model_from_dict():
    USER_ID = 1
    USER_EMAIL = "test@test.com"
    USER_PASSWORD = "secret"

    user_dict = {"id": USER_ID, "email": USER_EMAIL, "password": USER_PASSWORD}
    user = User.from_dict(user_dict)

    assert user.id == USER_ID
    assert user.email == USER_EMAIL
    assert user.password == USER_PASSWORD
