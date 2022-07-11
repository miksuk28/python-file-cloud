from flask import Blueprint, jsonify, request, abort
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
        users.create_user(
            username=username,
            password=json_data["password"],
            email=json_data["email"],
            disabled=json_data.get("blockLogin", False),
            fname=json_data.get("fname"),
            lname=json_data.get("lname")
        )
        return jsonify({"message": f"User {username} was created successfully"}), 201
    
    except exc.UserAlreadyExists:
        return jsonify({"error": f"User {username} already exists"}), 409

    except exc.EmailAlreadyInUse:
        return jsonify({"error": f"Email {json_data['email']} is already in use"}), 409


@users_blueprint.route("/<path:username>", methods=["GET"])
def get_user_by_username(username):
    try:
        user = users.get_user(username)
        return jsonify(user)

    except exc.UserDoesNotExist:
        return jsonify({"error": f"User {username} does not exist"}), 404


@users_blueprint.route("/", methods=["GET"])
def query_users():
    fname = request.args.get("fname", default="")
    lname = request.args.get("lname", default="")
    fetch = request.args.get("fetch", type=int)

    results = users.query_users(fname, lname, fetch)

    return jsonify({"result": results})


@users_blueprint.route("/<path:username>", methods=["DELETE"])
def delete_user_by_username(username):
    try:
        users.delete_user(username)
        return jsonify({"message": f"User {username} has been deleted"}), 204
    
    except exc.UserDoesNotExist:
        return jsonify({"error": f"User {username} does not exist"}), 404