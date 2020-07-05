print('\033[1;33m{=== EXERCÍCIO 063 ===}\033[m')
print('\033[1m=-=-=' * 12)
print('{}SEQUENCIA DE FIBONACCI'.format(' ' * 17))
n = int(input('Digite o número de termos de sua Sequência de Fibonacci: '))
t_1 = 0
t_2 = 1
print('{} - {} '.format(t_1, t_2), end ='')
cont = 3
while cont <= n:
    t_3 = t_1 + t_2
    t_1 = t_2
    t_2 = t_3
    print('- {} '.format(t_3), end='')
    cont += 1
print('')
print('=-=-=' * 12)
print('\033[1;33m{=== FINALIZADO ===}')

