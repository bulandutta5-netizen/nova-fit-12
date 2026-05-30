with open('preview.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        if 'const Chatbot' in line or 'Chatbot = ' in line:
            print(f'{i}: {line.strip()}')
