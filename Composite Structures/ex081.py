print('\033[1;33m{=== EXERCÍCIO 081 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{} Extraindo dados de uma Lista'.format(' ' * 12).upper())
print('=-=-=' * 10)
lista = []
while True:
    lista.append(int(input('Digite um número inteiro: ')))
    tipo = input('QUER CONTINUAR? [S/N] ').upper().strip()[0]
    if tipo in 'Nn':
        break
    if tipo not in 'SsNn':
        print('Opção inválida. Tente novamente.')
print('=-=-=' * 10)
print(lista)
print(f'Você digitou {len(lista)} números inteiros.')
print('Os valores em Ordem Crescente: ', sorted(lista))
print('Os valores em Ordem Decrescente: ', sorted(lista, reverse=True))
if 5 in lista:
    print('O número 5 foi encontrado na lista.')
else:
    print('O número 5 NÂO foi encontrado na lista.')
print('\033[1;33m{=== FINALIZADO 081 ===}')
