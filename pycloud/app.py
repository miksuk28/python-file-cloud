from flask import Flask, Blueprint
from blueprints.users import users_blueprint as users

app = Flask(__name__)

app.register_blueprint(users, url_prefix="/users")

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)