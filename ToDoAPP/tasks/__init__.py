from flask import Blueprint

tasks_bp = Blueprint('tasks', __name__)

from ToDoAPP.tasks import tasks
