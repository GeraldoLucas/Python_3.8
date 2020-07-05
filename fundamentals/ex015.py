print('\033[1;33m === EXERCÍCIO 015 === \033[m')
dias = int(input('\033[1mPor quantos dias o carro foi alugado?'))
km = float(input('Quantos quilômetros foram percorridos com o carro?'))
preco = (60.00 * dias) + (0.15 * km)
print('O valor total pelos {} dias de viagem \nSomados aos {:.0f}KM percorridos equivale à {}R$'.format(dias, km, preco))
print('\033[1;33m === FINALIZADO 015 === \033[m')



