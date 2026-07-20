"""
本地开发环境一键初始化全部数据表
生产环境使用Neon云端库，使用flask db migrate/upgrade
"""
from app import create_app
from extensions import db

app = create_app()

with app.app_context():
    db.create_all()
    print("✅ 所有业务数据表创建完成！")
