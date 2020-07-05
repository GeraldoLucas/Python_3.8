print('\033[1;33m{=== EXERCÍCIO 075 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{} Análise de dados em uma Tupla'.format(' ' * 10).upper())
print('=-=-=' * 10)
t = (int(input('Digite um número inteiro: ')),
     int(input('Digite mais um número inteiro: ')),
     int(input('Digite outro número inteiro: ')),
     int(input('Digite o último número inteiro: ')))

print(t)
n = t.count(9)
print(f'O número 9 apareceu {n} vezes.' if n > 1 else f'O número 9 apareceu {n} vez.')
if 3 in t:
    print(f'O primeiro valor 3 foi digitado na {t.index(3) + 1}° posição.')
else:
    print('Não foi digitado nenhum número 3 na lista.')
print('Os números pares digitados são ', end='')
for par in t:
    if par % 2 == 0:
        print(par, end=' | ')
print('\033[1;33m{=== FINALIZADO 075 ===}')
