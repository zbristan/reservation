from flask import Blueprint

# Define the blueprint
main = Blueprint('main', __name__)

from . import routes
