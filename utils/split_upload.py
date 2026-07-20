import os
from utils.file_tool import safe_mkdir

def split_save(cache_dir: str, file_md5: str, chunk_idx: int, chunk_data):
    """保存单个分片"""
    safe_mkdir(cache_dir)
    chunk_path = os.path.join(cache_dir, f"{file_md5}_{chunk_idx}.chunk")
    with open(chunk_path, "wb") as f:
        f.write(chunk_data)

def merge_chunk(cache_dir: str, file_md5: str, total_chunk: int, out_path: str) -&gt; bool:
    """合并所有分片"""
    chunk_paths = []
    for i in range(total_chunk):
        p = os.path.join(cache_dir, f"{file_md5}_{i}.chunk")
        if not os.path.exists(p):
            return False
        chunk_paths.append(p)

    with open(out_path, "wb") as out_f:
        for p in chunk_paths:
            with open(p, "rb") as in_f:
                out_f.write(in_f.read())
            os.remove(p)
    return True
