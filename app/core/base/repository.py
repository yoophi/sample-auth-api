from abc import ABC, abstractmethod


class BaseRepository(ABC):
    @abstractmethod
    def authenticate(self, email, password):
        pass
