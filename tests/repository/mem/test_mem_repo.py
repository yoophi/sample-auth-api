import pytest

from app.core.domain.user import User
from app.repository.mem import MemRepo


@pytest.fixture
def data_dicts():
    return [
        {"id": 1, "email": "test1@example.com", "password": "secret1"},
        {"id": 2, "email": "test2@example.com", "password": "secret2"},
        {"id": 3, "email": "test3@example.com", "password": "secret3"},
        {"id": 4, "email": "test4@example.com", "password": "secret4"},
        {"id": 5, "email": "test5@example.com", "password": "secret5"},
    ]


@pytest.fixture
def repo(data_dicts):
    return MemRepo(data_dicts)


@pytest.fixture
def domain_users(data_dicts):
    return [User.from_dict(d) for d in data_dicts]


def test_repository_user_authenticate(repo, domain_users):
    user = domain_users[0]
    response = repo.authenticate(user.email, user.password)
    assert bool(response) is True
    assert response == user
