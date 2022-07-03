from flask import Blueprint, jsonify
from modules.usermanager import UserManager

users = UserManager(token_validity=120, global_token_block=0, allow_admin_creation=True)
users_blueprint = Blueprint("users", __name__)

@users_blueprint.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "Hello World, from the users Blueprint"})


