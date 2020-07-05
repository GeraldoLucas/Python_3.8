print('\033[1;33m{=== EXERCÍCIO 097 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{}  Um print especial'.format(' ' * 13).upper())
print('=-=' * 10)


def texto(txt):
    borda = len(txt) + 4
    print('~' * borda)
    print(f'  {txt}')
    print('~' * borda)


texto('Olá, mundo!')
texto('Ótimo, dia. Vamos programar!')
texto('Python na área. ><')

print('\033[1;33m{=== FINALIZADO 097 ===}')
