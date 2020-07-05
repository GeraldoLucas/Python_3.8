print('\033[1;33m{=== EXERCÍCIO 058 ===}\033[m')
from random import randint
import time
comp = randint(0, 10)
print('\033[1m=-=-=-= PENSANDO EM UM NÚMERO... =-=-=-=')
time.sleep(1)
acertou = False
count = 0
while not acertou:
    jog = int(input('Jogador dê o seu palpite: '))
    count += 1
    if comp == jog:
        acertou = True
        print('Você acertou o número {} com {} tentativas!'.format(jog, count))
    else:
        if comp > jog:
            print('Você errou, um pouco MAIS...')
        elif comp < jog:
            print('Você errou, um pouco MENOS...')
print('\033[1;33m === FINALIZADO 058 ===')

