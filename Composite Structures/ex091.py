print('\033[1;33m{=== EXERCÍCIO 091 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{}  Jogo de Dados em Python'.format(' ' * 13).upper())
print('=-=-=' * 10)
import time
from time import sleep
import random
from random import randint
from operator import itemgetter
dado = dict()
rank = list()
for c in range(1, 5):
    dado[f'{c}°jogador'] = str(f'{c}°Jogador: DADO {randint(1,6)}')
for v in dado.values():
    print(v)
    sleep(1)
print('=-=-=' * 8)
print('   =-=   RANKING DOS JOGADORES   =-=')
rank = sorted(dado.values(), key=itemgetter(0), reverse=True)
for i, v in enumerate(rank):
    print(f'{i+1}° Lugar = {v[0]} {v[1]} PONTOS')
print('=-=-=' * 8)
print('ERROR')
print('\033[1;33m{=== FINALIZADO 091 ===}')


