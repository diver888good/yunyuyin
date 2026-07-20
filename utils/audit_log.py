from flask import request
from business_service.audit_service import AuditService

def add_audit_log(user_id: int, desc: str):
    """快速添加审计日志"""
    ip = request.remote_addr
    method = request.method
    path = request.path
    AuditService.add_log(user_id, ip, method, path, desc)
