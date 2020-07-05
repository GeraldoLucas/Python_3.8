print('\033[1;33m{=== EXERCÍCIO 045 ===}\033[m')
from random import randint
import time
print('\033[1;35m=-='*16)
print('{:17}JOKENPÔ ONLINE'.format(''))
print('\033[1;35m=-=\033[m'*16)
print(('Jogador, já conhece as regras do jogo? Então vamos lá!.'.upper()))
lista = ('PEDRA', 'PAPEL', 'TESOURA')
comp = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
jogador = int(input('JOGADOR, escolha uma opção:'))

print('JO...')
time.sleep(1)
print('{:5}KEN...'.format(''))
time.sleep(1)
print('{:11}PÔ!!!'.format(''))
time.sleep(1)
if comp == 0:
    if jogador == 0:
        print('EMPATE, JOGUEM NOVAMENTE!')
    elif jogador == 1:
        print('\033[1;36mO JOGADOR VENCEU!\033[m')
    elif jogador == 2:
        print('\033[1;31mO COMPUTADOR VENCEU!\033[m')
if comp == 1:
    if jogador == 0:
        print('\033[1;31mO COMPUTADOR VENCEU!\033[m')
    elif jogador == 1:
        print('EMPATE, JOGUEM NOVAMENTE!')
    elif jogador  == 2:
        print('\033[1;36mO JOGADOR VENCEU!\033[m')
if comp == 2:
    if jogador == 0:
        print('\033[1;36mO JOGADOR VENCEU!\033[m')
    elif jogador == 1:
        print('\033[1;31mO COMPUTADOR VENCEU!)\033[m')
    elif jogador == 2:
        print('EMPATE, JOGUEM NOVAMENTE!\033[m')
print('\033[1mO computador escolheu {}.'.format(lista[comp]))
print('O jogador escolheu {}.'.format(lista[jogador]))
print('\033[1;33m{=== FINALIZADO 045 ===}')
