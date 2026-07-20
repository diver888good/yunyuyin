from flask import Flask
from config import config_map
from extensions import db, migrate, login_manager, redis_store, init_celery
from app import register_all_blueprint
from middleware import register_middleware
import os

def create_app():
    # 读取环境
    env = os.getenv("FLASK_ENV", "development")
    app = Flask(__name__)
    app.config.from_object(config_map[env])

    # 初始化插件
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    redis_store.init_app(app)

    # 注册蓝图
    register_all_blueprint(app)

    # 注册中间件
    register_middleware(app)

    # 初始化Celery
    init_celery(app)

    return app
