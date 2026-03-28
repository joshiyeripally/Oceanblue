import os
import shutil

src = r"c:\Users\ASUS\Downloads\Oceanblue\images"
dst = r"c:\Users\ASUS\Downloads\Java Folder\Oceanblue\images"

# ensure dst exists
os.makedirs(dst, exist_ok=True)

for fname in os.listdir(src):
    src_file = os.path.join(src, fname)
    if os.path.isfile(src_file):
        shutil.copy2(src_file, dst)
        print(f"Copied {fname}")
