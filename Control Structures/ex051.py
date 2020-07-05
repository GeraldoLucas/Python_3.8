print('\033[1;33m{=== EXERCÍCIO 051 ===}\033[m')
a = int(input('\033[1mDigite o primeiro termo da PA:'))
r = int(input('Digite a razão da PA:'))
fim = a + (9*r)
print('Sua PA tem 10 termos, como termo inicial {} e razão {}.'.format(a, r))
for c in range(a, fim + 1, r):
    print(c, end=', ')
print('FIM')