print('\033[1;33m === EXERCÍCIO 023 === \033[m')
num = int(input('\033[1mDigite um número inteiro:'))
#n = str(num)
u = (num // 1 % 10)
d = (num //10 % 10)
c = (num //100 % 10)
m = (num // 1000 % 10)
print('Analisando as informações...')
print('Unidade:{}'.format(u))
print('Dezena:{}'.format(d))
print('Centena:{}'.format(c))
print('Milhar:{}'.format(m))
print('\033[1;33m === FINALIZADO 023 === \033[1m')





