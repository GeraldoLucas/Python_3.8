print('\033[1;33m{=== EXERCÍCIO 064 ===}\033[m')
print('\033[1m=-=-=' * 11)
print('{}TRATAMENTO DE VALORES '.format(' '* 15))
print('=-=-='*11)
print('-.- DIGITE [ 0 ] PARA PARAR -.-')
n = int(input('Digite um número inteiro: '))
contador = 0
cont = 0
while n != 0:
    contador += 1
    cont = cont + n
    n = int(input('Digite um número inteiro: '))
print('A soma dos {} valores informados é igual à {}.'.format(contador ,cont))
print('\033[1;33m{=== FINALIZADO 064 ===}')
