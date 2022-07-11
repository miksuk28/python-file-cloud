from flask import Flask, Blueprint, jsonify
from blueprints.users import users_blueprint

app = Flask(__name__)

app.register_blueprint(users_blueprint, url_prefix="/admin/users")


@app.errorhandler(500)
def internal_server_error(e):
    print(f"Internal Server Error:\n{e}\n")
    return jsonify(
        {"error": "An unknown internal server has occured. Please try again, and contact the admin if the error persists"}
    )


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)