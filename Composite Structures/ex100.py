print('\033[1;33m{=== EXERCÍCIO 100 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{} Funções para sortear e somar '.format(' ' * 9).upper())
print('=-=-=' * 10)
from random import randint
from time import sleep


def sorteio(lista):
    for c in range(0, 5):
        lista.append(randint(0, 10))
    print('Os valores sorteados foram:', end=' ')
    for n in lista:
        print(n, end=' ')
        sleep(1)
    print('')


lista = []
sorteio(lista)


def NumPar(pares):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
            soma = num + soma
    print('Os valores pares informados foram:', end=' ')
    for c in pares:
        print(c, end=' ')
        sleep(1)
    print('\nA soma dos valores pares é {}.'.format(soma))


pares = []
NumPar(pares)
sleep(2)
print('\033[1;33m{=== FINALIZADO 101 ===}')
