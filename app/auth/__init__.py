from flask import Blueprint

# Define the blueprint
auth = Blueprint('auth', __name__)

from . import routes
