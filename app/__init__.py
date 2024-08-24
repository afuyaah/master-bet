from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
from celery import Celery
from flask_migrate import Migrate
import os

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
celery = Celery(__name__, broker='redis://:rJPJx15gUdQSLJYMffFeY7NPOeLgfHcc@redis-11007.c8.us-east-1-3.ec2.redns.redis-cloud.com:11007/0')

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)
    celery.conf.update({'worker_hijack_root_logger': False})
    return celery

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate = Migrate(app, db)
    CORS(app)  # Initialize CORS if needed

    # Register Blueprints
    from .scraper.routes import scraping_bp
    from .auth.routes import auth_bp
    from .main.routes import main_bp

    app.register_blueprint(scraping_bp, url_prefix='/scraping')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp, url_prefix='/')

    # Create database tables
    with app.app_context():
        db.create_all()

    # Initialize Celery with the Flask app
    global celery
    celery = make_celery(app)

    return app

@login_manager.user_loader
def load_user(user_id):
    from app.main.models import User  # Adjust the import as needed
    return User.query.get(int(user_id))

# Example of a function to get a session
def get_session():
    # This creates a session that is scoped to the application context
    from sqlalchemy.orm import scoped_session, sessionmaker
    engine = db.engine
    Session = scoped_session(sessionmaker(bind=engine))
    return Session()
