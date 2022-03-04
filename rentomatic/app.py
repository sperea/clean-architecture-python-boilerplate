from flask import Flask

from rentomatic.rest import room
from rentomatic.flask_settings import DevConfig


def create_app(config_object=DevConfig):
    print ('creating app...')
    app = Flask(__name__)
    print('registering settings...')
    app.config.from_object(config_object)
    print('registering routes...')
    app.register_blueprint(room.blueprint)
    return app
