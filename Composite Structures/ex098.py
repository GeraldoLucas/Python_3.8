print('\033[1;33m{=== EXERCÍCIO 098 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{}  Função de Contador'.format(' ' * 13).upper())
print('=-=-=' * 10)
from time import sleep


def contador(a, b, c):
    for i in range(a, b + 1, c):
        print(i, end=' | ')
        sleep(0.5)
        if c > 0 and i >= b:
            print('FIM.')
        elif c < 0 and i <= b+2:
            print('FIM.')

print(' - Contador 0 até 10, 1 em 1: ')
contador(0, 10, 1)
print(' - Contador 20 até 0, 2 em 2: ')
contador(20, -2, -2)
print(' - Sua vez, PERSONALIZE o Contador: ')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passos: '))
contador(inicio, fim, passo)

print('\033[1;33m{=== FINALIZADO 098 ===}')
