print('\033[1;33m{=== EXERCÍCIO 070 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{}EMPÓRIO ASSIS '.format(' ' * 18))
print('=-=-=' * 10)
tipo = nome = preco = 0
cont = total = menor = 0
maior1000 = 0
barato = ''
while True:
    nome = str(input('Informe o nome do produto: '))
    preco = float(input('Informe o preço do produto: '))
    tipo = str(input('{}QUER CONTINUAR [S/N]? '.format(' ' * 5))).upper().strip()[0]
    cont = cont + 1
    total = total + preco
    if preco > 1000:
        maior1000 += 1
    if cont == 1 or menor > preco:
        menor = preco
        barato = nome
    if tipo in 'Nn':
        break
print('=-=-=' * 10)
print(f'Você informou {cont} produto.' if cont == 1 else f'Você informou {cont} produtos.')
print('O total de sua compra deu {:.1f}R$.'.format(total))
print('Ao todo {} produto(s) custam mais de 1000R$'.format(maior1000))
print('O produto mais barato foi {} que está custando {}R$.'.format(barato, menor))
print('\033[1;33m{=== FINALIZADO 70 ===}')
