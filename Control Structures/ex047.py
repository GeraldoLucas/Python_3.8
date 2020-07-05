print('\033[1;33m{=== EXERCÍCIO 047 ===}\033[m')
print('\033[1;36m=-=-'*12)
print('Aqui estão todos os números pares de 0 à 100:'.upper())
print('=-=-'*12, '\033[m')
for n in range(0, 101, 2):
    print(n, end = '|')
print('\n')
print('\033[1;33m=== FINALIZADO 047 ===')
