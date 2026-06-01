import os

file_path = r"C:\Users\Bikranta Dutta\OneDrive\Desktop\fit-nova-ai\login.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

print("Original size of login.html:", len(content))

# 1. Branding Translation
content = content.replace("Fit Nova", "NovaFit")
content = content.replace("FitNova", "NovaFit")
content = content.replace("FIT NOVA", "NOVAFIT")
content = content.replace("fit-nova-ai", "novafit-ai")
content = content.replace("fitnova_user", "novafit_user")
content = content.replace("fitnova_avatar", "novafit_avatar")
print("Branding translated in login.html.")

# 2. Re-color authentication base backgrounds to matching deep navy and violet glows
# --dark: #0A0A0A to #070710, --surface: #111111 to #0F0F24
content = content.replace("--dark: #0A0A0A;", "--dark: #070710;")
content = content.replace("--surface: #111111;", "--surface: #0F0F24;")
content = content.replace("background: #060608;", "background: #070710;")

# Save updated login.html
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated login.html successfully!")
