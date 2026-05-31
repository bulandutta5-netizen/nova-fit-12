import shutil
import os

base_dir = r"C:\Users\Bikranta Dutta\OneDrive\Desktop\fit-nova-ai"

files_to_sync = [
    (os.path.join(base_dir, "preview.html"), os.path.join(base_dir, "dist-preview", "index.html")),
    (os.path.join(base_dir, "login.html"), os.path.join(base_dir, "dist-preview", "login.html"))
]

print("Syncing active Desktop workspace to dist-preview...")
for src, dst in files_to_sync:
    if os.path.exists(src):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy2(src, dst)
        print(f"  [SUCCESS] Copied '{os.path.basename(src)}' to '{os.path.basename(dst)}' in dist-preview.")
    else:
        print(f"  [ERROR] Source '{src}' not found.")
