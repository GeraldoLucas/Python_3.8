print('\033[1;33m{=== EXERCÍCIO 072 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{}Número por Extenso'.format(' ' * 17).upper())
print('=-=-=' * 10)
import time
n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
     'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
     'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
     'dezessete', 'dezoito', 'dezenove', 'vinte'.upper())
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {n[num]}.')
        break
    else:
        print(f'O NÚMERO {num} NÃO É UM NÚMERO ENTRE 0 E 20! \n          TENTE NOVAMENTE!')
    time.sleep(1.5)
print('\033[1;33m{=== FINALIZADO 072 ===}')
