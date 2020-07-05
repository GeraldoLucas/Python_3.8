print('\033[1;33m{=== EXERCÍCIO 060 ===}\033[m')
import math
import time
from math import factorial
num = int(input('\033[1mInforme um número inteiro: '))
print('=-=-=' * 7)
print('{}CALCULANDO O SEU FATORIAL...'.format(' ' * 3))
print('=-=-=' * 7)
c = num
time.sleep(2)
while c > 0 :
    c -= 1
    print(c + 1,
          end = ' x ' if c >= 1 else f' = {factorial(num)}')
print('\n', '\033[1;33m{=== FINALIZADO 060 ===}')
