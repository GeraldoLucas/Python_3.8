print('\033[1;33m === EXERCÍCIO 036 === \033[m')
casa = float(input('\033[1mQual é o valor da casa? R$'))
salario = float(input('Qual é o salário do comprador? R$'))
anos = int(input('Qual o tempo, em anos, do pagamento da casa?'))
prest = (casa / (anos*12))
print('Para pagar uma casa no valor de {:.0f} em {} anos,'.format(casa, anos), end=' ')
print('o número de cada parcela mensal é igual à R${:.2f}.'.format(prest))
if prest >= 0.3*salario:
    print('\033[1;31mO empréstimo está NEGADO.\033[m')
#elif salario == (0.3*prest):
    #print('\033[1mSerá necessário RENEGOCIARMOS o empréstimo.\033[m')
else:
    print('\033[1;32mO empréstimo está APROVADO.\033[m')

