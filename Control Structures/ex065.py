print('\033[1;33m{=== EXERCÍCIO 065 ===}\033[m')
print('\033[1m=-=-='* 11)
print('{}MAIOR E MENOR VALOR'.format(' '* 17))
n = media = cont = soma = 0
maior = menor = 0
c = 'Ss' or 'Nn'
while c in 'Ss':
    n = int(input('Digite um número inteiro:'))
    c = str(input('Deseja continuar [S/N]?').upper().strip()[0])
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    print('=-=-=' * 11)
    #if c in 'Nn':
        #print('FIM')
media = soma/cont
print('Você informou {} números.'.format(cont).upper())
print('A média entre os eles é {:.1f}.'.format(media).upper())
print('O maior entre eles é {}.'.format(maior).upper())
print('O menor entre eles é {}.'.format(menor).upper())
print('\033[1;33m{=== FINALIZADO 065 ===}')

