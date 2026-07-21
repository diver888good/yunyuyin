#!/bin/bash
# PythonAnywhere 一键更新部署脚本

cd /home/music6/yunyuyin

# CI采用文件上传方式同步代码，注释git pull避免冲突
# git pull

# 加载.env环境变量（数据库、CST密钥，flask迁移必须）
source /home/music6/yunyuyin/.env

# 激活虚拟环境
source /home/music6/venv/bin/activate

# 安装/更新全部依赖
pip install -r requirements.txt

# 指定程序入口，执行数据库迁移
export FLASK_APP=wsgi.py
flask db upgrade

# 重启Celery异步任务
bash celery_start.sh

echo "✅ 网站部署重载完成"