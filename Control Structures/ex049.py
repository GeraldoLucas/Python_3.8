print('\033[1;33m{=== EXERCÍCIO 049 ===}\033[m')
n = int(input('\033[1mDigite um número inteiro: '))
print('Para o número {:.0f} esta é sua tabuada:'.format(n))
print('=-=-' * 5)
for c in range(0, 11):
    print('{} X {:0} = {:2}'.format(n, c, n*c))
print('=-=-' * 5)
print('\033[1;33m=== FINALIZADO 049 ===')





