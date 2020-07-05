print('\033[1;33m{=== EXERCÍCIO 083 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{} Validando expressões matemáticas'.format(' ' * 12).upper())
print('=-=-=' * 10)
exp = str(input('Digite uma Expressão Numérica: '))
lista = []
for simbolo in exp:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Expressão Numérica VÁLIDA!')
else:
    print('Expressão Numérica INVÁLIDA!')
print('\033[1;33m{=== FINALIZADO 083 ===}')
