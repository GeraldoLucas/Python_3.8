print('\033[1;33m === EXERCÍCIO 012 === \033[m')
p = float(input('\033[1mQual é o preço do produto?'))
print('Este produto tem um desconto atual de 5%!')
p2 = p * 0.95
print('Então, o preço atual do produto é de R${:.2f}'.format(p2))
print('\033[1;33m === FINALIZADO 012 === \033[m')

