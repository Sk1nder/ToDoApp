from flask import Flask
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap5
from pathlib import Path

from config import config

templates_dir = Path(__file__).resolve().parent / "templates"

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bootstrap = Bootstrap5()
ckeditor = CKEditor()

def create_app():

    app = Flask(__name__, template_folder=templates_dir)
    app.config.from_object(config)

    # Inicjalizacja Flask-Login
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # Ustawienie domyślnego widoku logowania

    # Inicjalizacja SQLAlchemy i Flask-Migrate
    db.init_app(app)
    migrate.init_app(app, db)

    # Inicjalizacja Flask-Bootstrap5 i Flask-CKEditor
    bootstrap.init_app(app)
    ckeditor.init_app(app)


    with app.app_context():
        from ToDoAPP.models import User, Task
        db.create_all()

        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(str(user_id))

        from ToDoAPP.routes import routes_bp
        from ToDoAPP.tasks import tasks_bp
        from ToDoAPP.auth import auth_bp

        app.register_blueprint(routes_bp, url_prefix='/')
        app.register_blueprint(tasks_bp, url_prefix='/')
        app.register_blueprint(auth_bp, url_prefix='/')

    return app
