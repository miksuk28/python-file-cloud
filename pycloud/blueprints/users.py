from flask import Blueprint, jsonify
from modules.usermanager import UserManager

users = UserManager()
users_blueprint = Blueprint("users", __name__)


@users_blueprint.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "Hello World, from the users Blueprint"})


