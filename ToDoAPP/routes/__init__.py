from flask import Blueprint

routes_bp = Blueprint('routes', __name__)

from ToDoAPP.routes import routes