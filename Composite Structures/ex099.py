print('\033[1;33m{=== EXERCÍCIO 099 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{}  Função que descobre o maior'.format(' ' * 9).upper())
print('=-=-=' * 10)
import random
from random import randint
from time import sleep


def maior(* num):
    cont = maior = 0
    print(' ')
    print('Analisando os valores passados..')
    for valor in num:
        print(valor, end=' ', flush=True)
        sleep(1)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'| Foram analisados {cont} valores.')
    print('O maior valor informado foi o número {}.'.format(maior))
    print(' ')


maior(1, 4, 5, 7, 8)
maior(1, 2, 3)
maior(0, 12, 14, 2, 5, 6, 8)

print('\033[1;33m{=== FINALIZADO 099 ===}')
