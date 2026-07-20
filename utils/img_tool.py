from PIL import Image
import os

def compress_image(src_path: str, out_path: str, quality=70):
    """图片压缩+保真"""
    if not os.path.exists(src_path):
        return
    img = Image.open(src_path)
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save(out_path, quality=quality, optimize=True)
