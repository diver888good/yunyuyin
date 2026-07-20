#!/bin/bash
# PythonAnywhere 一键更新部署脚本

cd /home/music6/yunyuyin

# 拉取最新代码
git pull

# 更新依赖
source /home/music6/venv/bin/activate
pip install -r requirements.txt --user

# 数据库迁移
flask db upgrade

# 重启Celery
bash celery_start.sh

echo "网站更新重载完成"
