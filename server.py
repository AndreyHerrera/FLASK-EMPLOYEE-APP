from flask import Flask
from flask_cors import CORS

from app.database.database import connection_database
from app.controllers.register.register import REGISTER
from app.controllers.login.login import LOGIN

APP = Flask(__name__)
CORS(APP)
APP.register_blueprint(REGISTER)
APP.register_blueprint(LOGIN)


if __name__ == '__main__':
    connection_database(any)
    APP.run(port = 3000, debug = True)