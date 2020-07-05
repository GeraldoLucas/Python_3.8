print('\033[1;33m{=== EXERCÍCIO 085 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{}  Listas com pares e ímpares '.format(' ' * 12).upper())
print('=-=-=' * 10)
num = []
par = []
impar = []
for c in range(1, 11):
    num.append(int(input(f'Digite o {c}° número inteiro: ')))
print(num)
for n in num:
    if n % 2 == 0:
        par.append(n)
        par.sort()
    elif n % 2 == 1:
        impar.append(n)
        impar.sort()
print(f'Lista em números pares: {par}.')
print(f'Lista em números ímpares: {impar}.')
print('\033[1;33m{=== FINALIZADO 085 ===}')
