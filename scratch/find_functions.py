with open('src/components/Chatbot.jsx', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        if 'getAdaptiveBotResponse' in line or 'compileBlueprint' in line:
            print(f'{i}: {line.strip()}')
