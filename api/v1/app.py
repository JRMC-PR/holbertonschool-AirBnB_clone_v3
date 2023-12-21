#!/usr/bin/python3
"""This module will return the current status of our API"""
from api.v1.views import app_views
from flask import Flask
import os
from models import storage


# Create a Flask instance
app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(self):
    """Closes the storage"""
    storage.close()


if __name__ == '__main__':
    HBNB_API_HOST = os.getenv('HBNB_API_HOST', default='0.0.0.0')
    HBNB_API_PORT = os.getenv('HBNB_API_PORT', default='5000')
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)

