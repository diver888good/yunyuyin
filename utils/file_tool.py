import os
import hashlib

def get_file_md5(file_path: str) -&gt; str:
    """获取文件MD5"""
    if not os.path.exists(file_path):
        return ""
    md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            md5.update(chunk)
    return md5.hexdigest()

def safe_mkdir(path: str):
    """安全创建文件夹"""
    if not os.path.exists(path):
        os.makedirs(path)
