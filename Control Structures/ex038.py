print('\033[1;33m{=== EXERCÍCIO 038 ===}\033[m')
n1 = int(input('\033[1;34mDigite o primeiro número inteiro:'))
n2 = int(input('\033[1;31mDigite o segundo número inteiro:\033[m'))
if n1 > n2:
    print('\033[1mO PRIMEIRO valor, {}, é o maior.'.format(n1))
elif n2 > n1:
    print('\033[1mO SEGUNDO valor, {}, é o maior.'.format(n2))
elif n1 == n2:
    print('\033[1mOs dois valores são iguais.')
print('\033[1;33m{=== FINALIZADO 038 ===}')

