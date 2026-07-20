FROM python:3.10-slim

WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# 复制依赖清单
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 拷贝项目源码
COPY . .

# 开放端口
EXPOSE 5000

# 生产启动命令
CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app"]
