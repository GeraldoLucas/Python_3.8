print('\033[1;33m{=== EXERCÍCIO 066 ===}\033[m')
print('\033[1m=-=-=' * 11)
print(f'{" " * 15} VÁRIOS NÚMEROS EM FLAG')
print('=-=-=' * 11)
n = cont = soma = 0
while True:
    n = int(input('DIGITE UM NÚMERO INTEIRO,'
                  ' [0] PARA SAIR: '))
    cont = cont + 1
    soma = soma + n
    if n == 0 or n == '':
        break
print(f'Você informou {cont - 1} valores inteiros.')
print(f'A soma dos números é igual a {soma}.')
print('\033[1;33m{=== FINALIZADO 066===}')