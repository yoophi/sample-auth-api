from app.core.response_objects import ResponseSuccess


class UserAuthenticateUseCase:
    def __init__(self, repo):
        self._repo = repo

    def execute(self, request):
        email = request.email
        password = request.password

        result = self._repo.authenticate(email, password)
        return ResponseSuccess(result)
