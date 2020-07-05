print('\033[1;33m{=== EXERCÍCIO 087 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{} Mais sobre Matriz em Python'.format(' ' * 12).upper())
print('=-=-=' * 10)
lista = [[], [], []]
soma_pares = soma_impares = 0
soma_coluna = 0
maior_linha = 0
for l in range(0,3):
    for c in range(0, 3):
        lista[l].append(int(input(f'Digite um número inteiro para {[l, c]}: ')))
print('=-=-=' * 10)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^5}]', end='')
        if lista[l][c] % 2 == 0:
            soma_pares += lista[l][c]
        else:
            soma_impares += lista[l][c]
    print()
print('Soma dos Pares: ', soma_pares)
print('Soma dos Ímpares: ', soma_impares)
for l in range(0,3):
    soma_coluna += lista[l][2]
print(f'A soma dos valores da 3° coluna é {soma_coluna}.')
print(f'O maior valor 2° linha é {max(lista[1])}.')
print('\033[1;33m{=== FINALIZADO 087 ===}')
