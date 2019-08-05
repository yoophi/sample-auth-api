from app.core.base.repository import BaseRepository


class SqlaRepo(BaseRepository):
    def authenticate(self, email, password):
        return None
