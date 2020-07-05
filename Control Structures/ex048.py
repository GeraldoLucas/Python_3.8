print('\033[1;33m{=== EXERCÍCIO 048 ===}\033[m')
import math
print('\033[1;36m=-=-' * 12)
print('Esta é a soma entre todos os números ímpares\nque são multiplos de 3, no intervalo de 1 à 500:')
print('=-=-'*12,'\033[m')
soma = 0
count = 0
for n in range(0, 501):
    if n % 2 != 0:
        if n % 3 == 0:
            print(n, end=', ')
            soma = soma + n
            count = count + 1
print('')
print('A soma de todos os {:.0f} valores solicitados é igual à {:.0f}.'.format(count, soma))
print('\033[1;33m === FINALIZADO 048 ===')




