#!/bin/bash
# 加载密钥环境变量
source /home/music6/yunyuyin/.env

# 清理旧celery进程
pkill -f "celery worker"
pkill -f "celery beat"

# 激活虚拟环境并进入项目目录
source /home/music6/venv/bin/activate
cd /home/music6/yunyuyin

# celery入口 wsgi.celery
celery -A wsgi.celery worker --loglevel=info --detach
celery -A wsgi.celery beat --loglevel=info --detach

echo "✅ Celery Worker + Beat 启动完成"