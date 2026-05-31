import re

file_path = r"C:\Users\Bikranta Dutta\OneDrive\Desktop\fit-nova-ai\preview.html"

search_terms = ['activeTab', 'sidebar', 'nav', 'bottom-nav', 'bottom nav', 'DashboardCard']

print("Searching preview.html structure...")

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")

# Let's search for React Component definitions or main state
for idx, line in enumerate(lines, 1):
    # Find activeTab useState definition
    if 'useState(' in line and 'activeTab' in line:
        print(f"Found activeTab definition at line {idx}: {line.strip()}")
    
    # Find navigation definitions
    if 'id="sidebar"' in line or "id='sidebar'" in line:
        print(f"Found sidebar ID at line {idx}: {line.strip()[:120]}")
        
    if 'mobile' in line.lower() and ('nav' in line.lower() or 'menu' in line.lower()) and '<div' in line:
        print(f"Potential Mobile Nav container at line {idx}: {line.strip()[:120]}")
        
    if 'activeTab ===' in line or 'activeTab===' in line:
        # Just show some instances to see how tabs are switched
        if idx % 50 == 0:
            print(f"ActiveTab switch check at line {idx}: {line.strip()[:100]}")
