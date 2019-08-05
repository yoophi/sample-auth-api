from unittest import mock

import pytest

from app.core.domain import User
from app.core.request_objects.user import UserAuthenticateRequestObject
from app.core.use_cases import UserAuthenticateUseCase

USER_ID = 1
USER_EMAIL = "test@test.com"
USER_PASSWORD = "secret"


@pytest.fixture
def domain_user():
    return User.from_dict(
        {"id": USER_ID, "email": USER_EMAIL, "password": USER_PASSWORD}
    )


def test_user_authenticate_with_invalid_data(domain_user):
    repo = mock.Mock()
    repo.authenticate.return_value = domain_user

    uc = UserAuthenticateUseCase(repo)
    request = UserAuthenticateRequestObject.from_dict(
        {"email": USER_EMAIL, "password": USER_PASSWORD}
    )

    response = uc.execute(request)
    repo.authenticate.assert_called_with(USER_EMAIL, USER_PASSWORD)

    assert bool(response) is True
    assert response.value == domain_user
