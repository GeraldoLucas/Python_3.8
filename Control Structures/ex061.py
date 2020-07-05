print('\033[1;33m{=== EXERCÍCIO 061 ===}\033[m')
a = int(input('\033[1mDigite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
fim = a + 9*r
c = a
print('=-=-=' * 11)
print('{}PROGRESSÃO ARITMÉTICA...'.format(' '* 3))
while c <= fim:
    print(c, end=' | ')
    c += r
print('')
print('=-=-=' * 11)
print('\033[1;33m{=== FINALIZADO 061 ===}')


