print('\033[1;33m{=== EXERCÍCIO 046 ===}\033[m')
import emoji
import time
print('\033[36;1m- -' * 12)
print('{:10}CONTAGEM REGRESSIVA'.format(''))
print('- -' * 12)
#for c in range(0, 11, 1).__reversed__(): OU --->
for c in range(10, -1, -1):
    print(c)
    time.sleep(1)
print(emoji.emojize('{:10}\033[1;31m:fire:VIVA O ANO NOVO!:fire:'.format('')))













