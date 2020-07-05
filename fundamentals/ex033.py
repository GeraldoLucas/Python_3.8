print('\033[1;33m === EXERCÍCIO 033 === \033[m')
a = float(input('\033[1mDigite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o último número:: '))
if a > b >= c or a > c >= b:
    print('{} é o maior número!'.format(a))
if b > a >= c or b > c>= a:
    print('{} é o maior número!'.format(b))
if c > a >= b or c > b>=a:
    print('{} é o maior número!'.format(c))
else:
    print('Não existe um número maior que o outro, os 3 números são iguais.')
print('\033[1;33m === FINALIZADO 033 === \033[m')

