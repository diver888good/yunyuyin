# 云愈音 - PythonAnywhere 部署手册

## 部署顺序
1. GitHub 推送完整源码
2. Neon 创建数据库、获取 DATABASE_URL
3. CST 创建存储桶、建好7层目录
4. PA 终端 git clone 代码
5. 配置 .env 密钥
6. 安装依赖、数据库迁移
7. 启动 Celery 任务
8. 绑定 Web 站点、Reload 上线

## 目录
/home/music6/
├── yunyuyin/     # 项目源码
├── venv/         # 虚拟环境
└── local_temp_cache # 临时分片目录

## 运维命令
bash pa_reload.sh    # 一键更新网站
bash celery_start.sh # 重启异步任务
bash clean_storage.sh # 清理过期文件
