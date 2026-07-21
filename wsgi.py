from app import create_app
from extensions import celery
import os

# 读取.env中的运行环境
FLASK_ENV = os.getenv("FLASK_ENV", "development")
app = create_app(FLASK_ENV)

# Flask配置同步至Celery
celery.conf.update(app.config)

# 异步任务支持Flask上下文（数据库/配置读取必备）
TaskBase = celery.Task
class ContextTask(TaskBase):
    abstract = True
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return TaskBase.__call__(self, *args, **kwargs)
celery.Task = ContextTask

if __name__ == "__main__":
    app.run()