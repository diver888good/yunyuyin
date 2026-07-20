# GitHub CI/CD 自动化说明

## 三条流水线
1. deploy_pa.yml
   推送main分支自动同步代码到PA、重载网站

2. db_backup.yml
   每日北京时间0点自动备份Neon数据库，上传CST

3. storage_sync.yml
   static静态资源变更自动同步至CST存储桶

## 所需 Secrets
PA_HOST
PA_USER
PA_SSH_KEY
CST_AK
CST_SK
CST_BUCKET
DATABASE_URL
