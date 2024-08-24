#app/celery.py
from celery import Celery
from app import create_app

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)
    return celery

# Initialize Flask app
app = create_app()

# Initialize Celery
celery = make_celery(app)

# Export Celery instance
__all__ = ('celery',)


