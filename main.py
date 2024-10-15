import os
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from src.settings.oauth import oauth

from src.settings.database import Init_database
from routers import RegisterUSerRouter


app = Flask(__name__)

if os.getenv('DEBUG'):
    app.config.from_object('src.settings.config.Development')
else:
    app.config.from_object('src.settings.config.Production')

# Si la aplica no va a ser publica cambiar origins
CORS(app)

jwt = JWTManager(app)

RegisterUSerRouter(app)

Init_database(app)

oauth.init_app(app)

if __name__ == '__main__':
    app.run()