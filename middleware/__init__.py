from flask import request, g
from business_service.audit_service import AuditService
import time

def register_middleware(app):

    @app.before_request
    def before_request():
        g.start_time = time.time()

    @app.after_request
    def after_request(resp):
        try:
            user_id = 0
            if hasattr(g, "user") and g.user:
                user_id = g.user.id

            ip = request.remote_addr
            method = request.method
            path = request.path
            desc = f"访问路由: {path}"

            # 仅记录业务接口，过滤静态资源
            if not path.startswith("/static"):
                AuditService.add_log(user_id, ip, method, path, desc)
        except Exception:
            pass
        return resp
