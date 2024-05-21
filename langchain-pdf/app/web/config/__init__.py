import os
from dotenv import load_dotenv

root_dir = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(root_dir, ".env")
load_dotenv(dotenv_path)
print("------------------------->", os.environ)


class Config:
    SESSION_PERMANENT = True
    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
    UPLOAD_URL = os.environ["UPLOAD_URL"]
    CELERY = {
        "broker_url": os.environ.get("REDIS_URI", False),
        "task_ignore_result": True,
        "broker_connection_retry_on_startup": False,
    }
