#!/bin/bash
source /home/music6/venv/bin/activate
cd /home/music6/yunyuyin

python -c "from tasks.clean_storage_task import clean_expire_storage; clean_expire_storage.delay()"

echo "过期资源清理任务已触发"
