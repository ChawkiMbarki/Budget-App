"""
    Entry point for the main app package
"""

from flask import Flask
from .controllers.main import main_bp
from .controllers.users import user_bp

def create_app():
    """ Creates an instance of the Flask application """

    app = Flask(__name__)
    app.secret_key = "dsfoqsdfoihqsdfkijqسبsidf54qdf54rt8ù;,:jkàèà-سيب"
    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp)
    return app
