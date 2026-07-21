#!/bin/bash
# PythonAnywhere 一键更新部署脚本

cd /home/music6/yunyuyin

# CI采用文件上传方式同步代码，注释git pull避免冲突
# git pull

# 激活虚拟环境，更新依赖
source /home/music6/venv/bin/activate
pip install -r requirements.txt

# 数据库迁移
flask db upgrade

# 重启Celery异步任务
bash celery_start.sh

echo "网站更新重载完成"
