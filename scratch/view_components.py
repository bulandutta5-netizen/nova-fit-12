import re

file_path = r"C:\Users\Bikranta Dutta\OneDrive\Desktop\fit-nova-ai\preview.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's search for lines like "const Component = ..." or "function Component ..."
matches = re.finditer(r'(const|function)\s+([A-Z][a-zA-Z0-9_]*)\s*=\s*(?:\(\s*\)\s*=>|function|\([^)]*\)\s*=>)', content)

print("--- REACT COMPONENTS DEFINED ---")
for m in matches:
    # Find the line number
    char_index = m.start()
    line_num = content[:char_index].count('\n') + 1
    print(f"Component: {m.group(2)} at Line {line_num}")

# Also find where ReactDOM.render / createRoot / mounting happens
mount_match = re.search(r'ReactDOM\.', content)
if mount_match:
    line_num = content[:mount_match.start()].count('\n') + 1
    print(f"Mounting: {mount_match.group(0)} at Line {line_num}")
