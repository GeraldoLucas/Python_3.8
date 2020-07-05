print('\033[1;33m{=== EXERCÍCIO 076 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{} Lista de Preços com Tupla'.format(' ' * 12).upper())
print('=-=-=' * 10)
cont = 0
lista = ('Lápis', 1.00, 'Caneta', 1.10, 'Borracha', 0.5, 'Papel A4 ', 5.00, 'Computador', 1200,
         'Calculadora', 2.30, 'Régua', 1.5, 'Garrafa', 6.00, 'Tesoura', 2.50, 'Álcool', 5.00)
for c in range(0, len(lista), 2):
    print(f'{lista[c]:<40}', f'R${lista[c + 1]:>7}')
    cont = cont + lista[c+1]
print('Há {} produtos na lista.                 R${:.2f}'.format(len(lista), cont))
print('=-=-=' * 10)
print('\033[1;33m{=== FINALIZADO 076 ===}')
