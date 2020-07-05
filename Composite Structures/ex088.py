print('\033[1;33m{=== EXERCÍCIO 088 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{} Palpites para a Mega Sena '.format(' ' * 12).upper())
print('=-=-=' * 10)
import time
from random import sample
qt = int(input('Quantos jogos você quer que sorteie? '))
print(f'=-=-=-=   Sorteando {qt} Jogos da Mega Sena  =-=-=-=')
lista = []
for c in range(1, qt+1):
    r = sample(range(0,61), 6)
    lista.append(r[:])
    print(f'JOGO {c}: ', r)
    time.sleep(1)
print('\033[1;33m{=== FINALIZADO 088 ===}')

