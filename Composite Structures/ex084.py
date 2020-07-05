print('\033[1;33m{=== EXERCÍCIO 084 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{} Lista composta e análise de dados'.format(' ' * 12).upper())
print('=-=-=' * 10)
lista = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Digite o nome da pessoa: ').strip().capitalize()))
    dados.append(float(input('Digite o seu peso: KG ')))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    tipo = input('QUER CONTINUAR? [S/N] ').upper().strip()[0]
    if tipo in 'Nn':
        break
print(lista)
print(f'Ao todo você cadastrou {len(lista)} pessoa.' if len(lista) == 1 else 'Ao todo você cadastrou {} pessoas.'.format(len(lista)))
print(f'O maior peso foi de {maior}Kg, peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}', end='. ')
print('')
print(f'O menor peso foi de {menor}Kg, peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}', end='. ')
print('\033[1;33m{=== FINALIZADO 084 ===}')




