from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_redis import FlaskRedis
from celery import Celery

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
redis_store = FlaskRedis()

login_manager.login_view = "auth.login"
login_manager.login_message = "请先登录"

def init_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['REDIS_URL'],
        broker=app.config['REDIS_URL']
    )
    celery.conf.update(app.config)
    app.celery = celery
    return celery
