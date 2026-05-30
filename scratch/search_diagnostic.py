filepath = r"C:\Users\Bikranta Dutta\.gemini\antigravity\scratch\fit-nova-ai\preview.html"

with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()

print("Searching for 'activeVisual'...")
for idx, line in enumerate(lines):
    if "activeVisual" in line:
        print(f"Line {idx+1}: {line.strip()}")
