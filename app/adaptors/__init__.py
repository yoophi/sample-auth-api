from app.core.request_objects.user import UserAuthenticateRequestObject
from app.core.use_cases import UserAuthenticateUseCase


class UserAdaptor:
    def __init__(self, repo):
        self.use_case = UserAuthenticateUseCase(repo)

    def authenticate(self, email, password):
        request = UserAuthenticateRequestObject(email=email, password=password)
        response = self.use_case.execute(request)
        return response.value
