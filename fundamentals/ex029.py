print('\033[1;33m === EXERCÍCIO 029 === \033[m')
v = float(input('\033[1mPor favor, digite sua velocidade:'))
if v > 80:
    print('AVISO: Velocidade máxima permitida 80 KM/H, você será multado!')
    print('A multa será 7,00R$ para cada Km acima do AVISO!')
    multa = 7 * (v % 80)
    print('O valor de sua multa é de {}R$'.format(multa))
else:
    print('AVISO: Velocidade máxima permitida 80KM/H, você não será multado! \nTenha um bom dia!')
print('\033[1;33m === FINALIZADO 029 === ')