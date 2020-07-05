print('\033[1;33m{=== EXERCÍCIO 102 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{}  Função para Fatorial'.format(' ' * 14).upper())
print('=-=-=' * 10)
from math import factorial
from time import sleep


def fatorial(num, show=False):
    print(f'O fatorial de {num} é igual a ', end='')
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x', end=' ')
            else:
                print(' = ', end=' ')
        f *= c
    return f


print(fatorial(5, show=True))

sleep(2)
print('\033[1;33m{=== FINALIZADO 102 ===}')
