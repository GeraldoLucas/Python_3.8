print('\033[1;33m{=== EXERCÍCIO 080 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{} Lista ordenada sem repetições'.format(' ' * 12).upper())
print('=-=-=' * 10)
lista = []
for cont in range(1, 6):
    num = int(input('Digite um número inteiro: '))
    if cont == 1 or num > lista[-1]:
        lista.append(num)
        print('Número adicionado ao FINAL da lista.')
    else:
        for posicao in range(len(lista)):
            if num <= lista[posicao]:
                lista.insert(posicao, num)
                print(f'Número adicionado na {posicao}° POSIÇÂO da lista.')
                break
print('=-=-=' * 10)
print(f'Sua lista está configurada: {lista}')
print('=-=-=' * 10)
print('\033[1;33m{=== FINALIZADO 080 ===}')



