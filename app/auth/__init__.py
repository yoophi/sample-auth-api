from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

from app import adaptors
from app.repository import current_repo

auth = Blueprint("auth", __name__)


@auth.route("/token", methods=["POST"])
def access_token():
    email = request.json.get("email")
    password = request.json.get("password")

    adaptor = adaptors.UserAdaptor(repo=current_repo)
    user = adaptor.authenticate(email, password)
    if user is None:
        return jsonify({"msg": "Invalid grant"}), 401

    access_token = create_access_token(identity=user.id)

    return jsonify({"access_token": access_token})


@auth.route("/validate-token", methods=["GET"])
@jwt_required
def validate_token():
    user_id = get_jwt_identity()
    return jsonify({"user_id": user_id})
