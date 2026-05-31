with open('preview.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        if 'onboardingFlow =' in line or 'onboardingFlow = [' in line:
            print(f'{i}: {line.strip()}')
