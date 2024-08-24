import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'a_very_secret_key_that_is_hard_to_guess')
    
    # Redis connection details
    REDIS_URL = os.environ.get('REDIS_URL', 'redis://:rJPJx15gUdQSLJYMffFeY7NPOeLgfHcc@redis-11007.c8.us-east-1-3.ec2.redns.redis-cloud.com:11007/0')

    # Celery configuration
    CELERY_BROKER_URL = REDIS_URL
    CELERY_RESULT_BACKEND = REDIS_URL

    # Celery beat schedule
    CELERY_BEAT_SCHEDULE = {
        'run-sports-spider-every-day': {
            'task': 'app.scraping.tasks.run_sports_spider',
            'schedule': 86400.0,  # 86400 seconds = 24 hours
        },
    }
    
    # SQLAlchemy configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///masterbet.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
