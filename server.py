"""
    The entry point to start the application
"""

from app import create_app

if __name__ == "__main__":
    create_app().run(debug = True)