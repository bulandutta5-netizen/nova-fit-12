filepath = r"C:\Users\Bikranta Dutta\.gemini\antigravity\scratch\fit-nova-ai\preview.html"

with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
for idx, line in enumerate(lines):
    if "onboardingFlow" in line:
        print(f"{idx+1}: {line.strip()[:140]}")
