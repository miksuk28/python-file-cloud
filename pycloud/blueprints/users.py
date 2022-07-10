from flask import Blueprint, jsonify, request
from modules.usermanager import UserManager
from modules.wrappers import json_validator
from modules.exceptions import usermanager_exceptions as exc
from blueprints.json_schemas.usermanager_schemas import UserManagerSchemas as schemas

users = UserManager(token_validity=120, global_token_block=0, allow_admin_creation=True)
users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "Hello World, from the users Blueprint"})


# Create User
@users_blueprint.route("/<path:username>", methods=["POST"])
@json_validator(schemas.register)
def create_user(username):
    json_data = request.get_json()

    try:
        users.create_user(username, json_data.get("password"))

        return jsonify({"message": f"User {username} was created successfully"})
    except exc.UserAlreadyExists:
        return jsonify({"error": f"User {username} already exists"}), 409