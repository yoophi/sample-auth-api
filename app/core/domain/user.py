class User:
    def __init__(self, id, email, password):
        self.id = id
        self.email = email
        self.password = password

    @classmethod
    def from_dict(cls, adict):
        return cls(id=adict["id"], email=adict["email"], password=adict["password"])

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()

    def to_dict(self):
        return {"id": self.id, "email": self.email, "password": self.password}
