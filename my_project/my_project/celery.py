import os

from celery import Celery
from common.configs.config import config as cfg

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
app = Celery(cfg.get("celery", "QUEUE"), broker=cfg.get("celery", "AMPQ_URL"))

if __name__ == "__main__":
    app.start()