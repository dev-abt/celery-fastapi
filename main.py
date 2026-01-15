from celery import Celery

from project import create_app

app = create_app()

celery = Celery(__name__, broker="redis://redis:6379/0", backend="redis://redis:6379/0")
