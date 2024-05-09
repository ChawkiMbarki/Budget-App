"""
    Entry point for the main app package
"""

from flask import Flask
from .controllers import main

def create_app():
    """ Creates an instance of the Flask application """

    app = Flask(__name__)
    app.secret_key = "dsfoqsdfoihqsdfkijqسبsidf54qdf54rt8ù;,:jkàèà-سيب"
    app.register_blueprint(main.main_bp)
    return app
