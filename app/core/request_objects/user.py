from app.core.request_objects import InvalidRequestObject, ValidRequestObject


class UserAuthenticateRequestObject(ValidRequestObject):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    @classmethod
    def from_dict(cls, adict):
        try:
            return cls(email=adict["email"], password=adict["password"])
        except KeyError:
            return InvalidRequestObject()
