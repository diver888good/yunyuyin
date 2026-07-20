import bcrypt

def encrypt_password(raw_pwd: str) -&gt; str:
    """密码bcrypt哈希加密"""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(raw_pwd.encode("utf-8"), salt).decode("utf-8")

def check_password(raw_pwd: str, hash_pwd: str) -&gt; bool:
    """密码校验"""
    return bcrypt.checkpw(raw_pwd.encode("utf-8"), hash_pwd.encode("utf-8"))
