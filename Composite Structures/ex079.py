print('\033[1;33m{=== EXERCÍCIO 079 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{} Valores únicos em uma Lista'.format(' ' * 12).upper())
print('=-=-=' * 10)
import time
lista = []
tipo = 0
num = 0
while True:
    num = int(input('Digite um número inteiro: '))
    lista.append(num)
    if lista.count(num) == 2:
        print('     VALOR DUPLICADO NÃO ADICIONADO.')
        lista.pop()
    tipo = input('DESEJA CONTINUAR? [S/N] ').upper().strip()[0]
    if tipo in 'Nn':
        break
    if tipo not in 'Ss':
        print('     OPÇÃO INVÁLIDA, TENTE NOVAMENTE!')
        lista.pop()
print('=-=-=' * 10)
print('VOCÊ DIGITOU OS VALORES: ', (sorted(lista)))
print('\033[1;33m{=== FINALIZADO 079 ===}')



