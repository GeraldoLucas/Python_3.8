print('\033[1;33m{=== EXERCÍCIO 067 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{}TABUADA 3.0'.format(' ' * 18))
print('=-=-=' * 10)
while True:
    num = int(input('Informe um número inteiro para ver sua tabuada: '))
    if num < 0:
        print('{}NÃO INFORMAMOS TABUADAS NEGATIVAS'.format(' ' * 8))
        break
    if num > 0:
        for cont in range(0, 11):
            print('{}{} x {} = {}'.format(' ' * 18, num, cont, num * cont))
print('=-=-=' * 10)
print('\033[1;33m{=== FINALIZADO 067 ===}')
