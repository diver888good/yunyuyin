from flask import Flask
from extensions import db, migrate, login_manager, redis_store, celery
from config import config_map

def create_app(env="development"):
    app = Flask(__name__)
    app.config.from_object(config_map[env])

    # 初始化所有扩展
    from extensions import init_extensions
    init_extensions(app)

    # 注册蓝图（蓝图内部自带url_prefix，注册时不要传第二个参数）
    from .auth import auth_bp
    from .voice import voice_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(voice_bp)

    # 新增根路由，解决首页404
    @app.route("/")
    def home_page():
        return """
        <h1>音乐疗愈平台</h1>
        <p><a href="/auth/login">前往登录页面</a></p>
        """

    return app
