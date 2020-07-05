print('\033[1;33m{=== EXERCÍCIO 050 ===}\033[m')
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('\033[1mDigite o {}° número inteiro:'.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} valores PARES e a soma deles é igual à {}.'.format(cont, soma))
print('\033[1;33m=== FINALIZADO 050 ===')