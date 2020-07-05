print('\033[1;33m === EXERCÍCIO 031 === \033[m')
d = float(input('\033[1mDigite a distância percorrida em quilômetros:'))
if d <= 200:
    p = (d * 0.50)
    print('O valor cobrado pelos {:.0f}Km rodados é igual a {}R$.'.format(d, p))
else:
    p2 = d * 0.45
    print('O valor estimado pelos {:.0f}Km rodados é igual a {}R$'.format(d, p2))
print('Pague na próxima agência. \nObrigado, tenha um bom dia!')
print('\033[1;33m === FINALIZADO 031 === \033[m')
