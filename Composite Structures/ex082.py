print('\033[1;33m{=== EXERCÍCIO 082 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{} Dividindo valores em várias listas'.format(' ' * 12).upper())
print('=-=-=' * 10)
lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um número inteiro: ')))
    tipo = str(input('QUER CONTINUAR? [S/N] ')).upper().strip()[0]
    if tipo in 'Nn':
        break
    if tipo not in 'SsNn':
        print('Opção inválida, número removido. Tente novamente.')
        lista.pop()
for posicao, valor in enumerate(lista):
    #print(posicao, num)
        if valor % 2 == 0:
            par.append(valor)
        elif valor % 2 == 1:
            impar.append(valor)
print('=-=-=' * 10)
print('Sua lista total: ', lista)
print('Sua lista somente com NÚMEROS PARES: ', par)
print('Sua lista somente com NÚMEROS ÍMPARES: ', impar)
print('\033[1;33m{=== FINALIZADO 082 ===}')

