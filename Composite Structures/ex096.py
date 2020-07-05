print('\033[1;33m{=== EXERCÍCIO 096 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{} Função que calcula área'.format(' ' * 13).upper())
print('=-=-=' * 10)


def area(larg, comp):
    t = larg * comp
    print(f'A ÁREA de um terreno {larg:.1f}m x {comp:.1f}m é igual a {t:.1f}m².')


a = float(input('Digite a LARGURA do terreno, em metros (m): '))
b = float(input('Digite o COMPRIMENTO do terreno, em metros (m): '))
area(a, b)

print('\033[1;33m{=== FINALIZADO 096 ===}')
