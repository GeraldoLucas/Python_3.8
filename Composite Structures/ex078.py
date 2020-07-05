print('\033[1;33m{=== EXERCÍCIO 078 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{} Maior e Menor valores na Lista'.format(' ' * 12).upper())
print('=-=-=' * 10)
lista = []
for pos, c in enumerate(range(1, 6)):
    lista.append(int(input(f'{" " * 13}Na {pos+1}° posição, temos: ')))
print('SUA LISTA NUMÉRICA:', lista)
print('=-=-=' * 9)
print(f'O maior valor digitado vale {max(lista)}, na {lista.index(max(lista))+1}° posição.'.upper())
print('=-=-=' * 9)
print(f'O menor valor digitado vale {min(lista)}, na {lista.index(min(lista))+1}° posição.'.upper())
print('=-=-=' * 9)
print('\033[1;33m{=== FINALIZADO 078 ===}')



