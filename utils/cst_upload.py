import os
from dotenv import load_dotenv
import requests

load_dotenv()

CST_AK = os.getenv("CST_AK")
CST_SK = os.getenv("CST_SK")
CST_UPLOAD_URL = os.getenv("CST_UPLOAD_URL")

def cst_upload_local_file(local_path: str, cst_key: str) -> str:
    """上传本地文件到CST"""
    if not os.path.exists(local_path):
        return ""
    with open(local_path, "rb") as f:
        data = f.read()
    return cst_upload_file_bytes(data, cst_key)

def cst_upload_file_bytes(file_bytes, cst_key: str) -> str:
    """字节流上传CST"""
    files = {"file": file_bytes}
    data = {
        "ak": CST_AK,
        "sk": CST_SK,
        "key": cst_key
    }
    res = requests.post(CST_UPLOAD_URL, data=data, files=files, timeout=30)
    res_json = res.json()
    if res_json.get("code") == 200:
        return res_json.get("url", "")
    return ""

def cst_delete_file(cst_url: str):
    """删除CST云端文件"""
    data = {
        "ak": CST_AK,
        "sk": CST_SK,
        "url": cst_url
    }
    requests.post(CST_UPLOAD_URL + "/delete", json=data, timeout=10)
