from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow

cors = CORS()
ma = Marshmallow()
jwt = JWTManager()
