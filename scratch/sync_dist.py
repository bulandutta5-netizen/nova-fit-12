import shutil
import os

files_to_sync = [
    (r"C:\Users\Bikranta Dutta\.gemini\antigravity\scratch\fit-nova-ai\preview.html", r"C:\Users\Bikranta Dutta\.gemini\antigravity\scratch\fit-nova-ai\dist-preview\index.html"),
    (r"C:\Users\Bikranta Dutta\.gemini\antigravity\scratch\fit-nova-ai\login.html", r"C:\Users\Bikranta Dutta\.gemini\antigravity\scratch\fit-nova-ai\dist-preview\login.html")
]

print("Syncing workspace to dist-preview...")
for src, dst in files_to_sync:
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"  [SUCCESS] Copied '{os.path.basename(src)}' to dist-preview.")
    else:
        print(f"  [ERROR] Source '{src}' not found.")
