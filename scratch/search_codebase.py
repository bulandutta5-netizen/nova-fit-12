import re

filepath = r"C:\Users\Bikranta Dutta\.gemini\antigravity\scratch\fit-nova-ai\preview.html"

search_terms = [
    "getAdaptiveBotResponse",
    "const Chatbot",
    "messages.map",
    "dashboard",
    "const Dashboard",
    "onCalculate",
    "login"
]

with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
for term in search_terms:
    print(f"\n--- Searching for: '{term}' ---")
    matches = 0
    for idx, line in enumerate(lines):
        if term in line:
            print(f"{idx+1}: {line.strip()[:120]}")
            matches += 1
            if matches >= 15:
                print("... (truncated)")
                break
