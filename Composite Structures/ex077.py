print('\033[1;33m{=== EXERCÍCIO 077 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{} Contando vogais em Tupla'.format(' ' * 12).upper())
print('=-=-=' * 10)
lista = ('APRENDER', 'PROGRAMAR', 'PYTHON', 'CURSO', 'GRATIS',
         'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
         'TRABALHADOR', 'FUTURO')
for c in lista:
    print(f'\nEm {c} temos como vogais: ', end='')
    for letra in c:
        if letra.upper() in 'AEIOU':
            print(letra, end='')
print('')
print('\033[1;33m{=== FINALIZADO 077 ===}')
