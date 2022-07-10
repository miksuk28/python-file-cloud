from flask import Flask, Blueprint
from blueprints.users import users_blueprint

app = Flask(__name__)

# TODO: Change this to /admin
app.register_blueprint(users_blueprint, url_prefix="/admin/users")

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)