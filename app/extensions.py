#app/extensions.py

from celery import Celery

def make_celery(app):
    celery = Celery(
        app.import_name,
        broker=app.config['CELERY_BROKER_URL'],
        backend=app.config['result_backend']  # Use 'result_backend' instead of 'CELERY_RESULT_BACKEND'
    )
    celery.conf.update(app.config)
    return celery
