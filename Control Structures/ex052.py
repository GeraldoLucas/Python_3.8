print('\033[1;33m{=== EXERCÍCIO 052 ===}\033[m')
n = int(input('\033[1mDigite um número inteiro: '))
cont = 0
for primo in range(1, n+1, 1):
    if n % primo == 0:
        print('\033[32m', end='')
        cont = cont + 1
    else:
        print('\033[31m', end='')
    print('{}'.format(primo), end=', ')
print(f'\nO número {n} foi divisível {cont} vezes.')
if cont > 2:
    print('\033[1;31mEsse NÃO é um número primo.')
else:
    print('\033[1;32mEsse É UM NÚMERO PRIMO!')
print('\033[1;33m')





