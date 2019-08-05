from app.core.base.repository import BaseRepository
from app.core.domain.user import User


class MemRepo(BaseRepository):
    def __init__(self, data):
        self._data = data

    def authenticate(self, email, password):
        for d in self._data:
            if d["email"] == email and d["password"] == password:
                return User.from_dict(d)

        return None
