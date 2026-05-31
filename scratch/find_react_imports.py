with open('preview.html', 'r', encoding='utf-8') as f:
    found = False
    for i, line in enumerate(f, 1):
        if 'const {' in line and ('useState' in line or 'useRef' in line) and i < 1470:
            print(f'{i}: {line.strip()}')
            found = True
    if not found:
        print("No destructuring found before line 1470")
