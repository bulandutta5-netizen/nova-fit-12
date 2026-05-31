with open('preview.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f, 1):
        if 'const Testimonials' in line or 'Testimonials = ' in line or '9.' in line or 'Testimonials' in line:
            if 'const ' in line or '//' in line:
                print(f'{i}: {line.strip()}')
