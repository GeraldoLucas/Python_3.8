print('\033[1;33m{=== EXERCÍCIO 086 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{} Matriz em Python'.format(' ' * 12).upper())
print('=-=-=' * 10)
matriz = [[], [], []]
for n in range(0, 3):
    for c in range(0, 3):
        matriz[n].append(int(input(f'Digite um número inteiro para {[n, c]}: ')))
print('=-=-=' * 10)
for n in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[n][c]:^4}]', end='')
    print()
print('=-=-=' * 10)
print('\033[1;33m{=== FINALIZADO 086 ===}')
