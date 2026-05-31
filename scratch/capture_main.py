import os
import subprocess

chrome_paths = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe")
]

chrome_path = None
for path in chrome_paths:
    if os.path.exists(path):
        chrome_path = path
        break

if not chrome_path:
    print("Chrome not found")
    exit(1)

local_url = "file:///C:/Users/Bikranta%20Dutta/.gemini/antigravity/scratch/fit-nova-ai/dist-preview/index.html"
screenshot_path = r"C:\Users\Bikranta Dutta\.gemini\antigravity\brain\b6e78f82-482c-40e5-9ae2-3207d17dfa04\homepage_luxury_preview.png"

cmd = [
    chrome_path,
    "--headless",
    "--disable-gpu",
    "--window-size=1280,1020",
    "--virtual-time-budget=5000",
    f"--screenshot={screenshot_path}",
    local_url
]

print(f"Running screenshot command: {' '.join(cmd)}")
try:
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=25)
    if os.path.exists(screenshot_path):
        print(f"Screenshot successfully captured at {screenshot_path}")
        print("Size:", os.path.getsize(screenshot_path), "bytes")
    else:
        print("Screenshot file was not generated.")
except Exception as e:
    print(f"Error: {e}")
