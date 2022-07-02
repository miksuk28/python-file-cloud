from flask import Blueprint, jsonify

uploads = Blueprint("uploads", __name__)

@uploads.route("/", defaults={"path": ""}, methods=["GET"])
@uploads.route("/<path:path>")
def test(path):
    return f"This is the path: {path}"
