from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_redis import FlaskRedis
from celery import Celery

# 全局扩展单例
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
redis_store = FlaskRedis()
celery = Celery(__name__)

# 登录配置
login_manager.login_view = "auth.login"
login_manager.login_message = "请先登录"

# 统一初始化所有扩展
def init_extensions(app):
    # 数据库
    db.init_app(app)
    migrate.init_app(app, db)
    # Redis
    redis_store.init_app(app)
    # 登录
    login_manager.init_app(app)
    # Celery 绑定配置
    # celery.conf.broker_url = app.config["REDIS_URL"]
    # celery.conf.result_backend = app.config["REDIS_URL"]
    # celery.conf.update(app.config)
    # 将 celery 挂载到 app 实例方便蓝图调用
    app.celery = celery
