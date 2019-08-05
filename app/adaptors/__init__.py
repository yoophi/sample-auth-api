from app.core.request_objects.user_auth_request_object import UserAuthRequestObject
from app.core.use_cases.user_authentication_use_case import UserAuthenticateUseCase


class UserAdaptor:
    def __init__(self, repo):
        self.use_case = UserAuthenticateUseCase(repo)

    def authenticate(self, email, password):
        request = UserAuthRequestObject(email=email, password=password)
        response = self.use_case.execute(request)
        return response.value
