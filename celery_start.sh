#!/bin/bash
# 后台启动Celery Worker & Beat

pkill -f "celery worker"
pkill -f "celery beat"

source /home/music6/venv/bin/activate
cd /home/music6/yunyuyin

celery -A app.celery worker --loglevel=info --detach
celery -A app.celery beat --loglevel=info --detach

echo "Celery 启动完成"
