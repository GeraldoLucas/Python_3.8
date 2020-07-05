print('\033[1;33m === EXERCÍCIO 028 === \033[m')
from random import randint
import time
compu = int(randint(0, 5))
print('\033[1;46m-=-\033[m'*15)
print('\033[1;36mPENSANDO... PENSANDO EM UM NÚMERO...\033[m')
print('\033[1;46m-=-\033[m'*15)
usuario = int(input('\033[1mJogador, em qual número eu pensei? Hehe...'))
print('PROCESSANDO...')
time.sleep(2)
if compu == usuario:
    print('Parabéns, você acertou o número {}!'.format(compu))
else:
    print('Sinto muito, você errou!Eu pensei em {} e você em {}'.format(compu, usuario))
print('\033[1;33m === FINALIZADO 028 === \033[m')




