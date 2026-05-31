with open('preview.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        if 'lucide' in line.lower():
            print(f'{i}: {line.strip()}')
