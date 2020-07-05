print('\033[1;33m{=== EXERCÍCIO 044 ===}\033[m')
p = float(input('\033[1mQual é o preço do produto? R$'))
print('=-='*20)
print('Existem no total 4 formas distintas de pagamento!'.upper())
print('[ 1 ] À vista no dinheiro ou cheque, com 10% de desconto.')
print('[ 2 ] À vista no cartão, com 5% de desconto.')
print('[ 3 ] Em até 2x no cartão, sem custo adicional.')
print('[ 4 ] Ou em 3x ou mais no cartão, com 20% de juros.')
print('=-='*20)
escolha = int(input('Selecione uma opção:'.upper()))
if escolha == 1:
    print('O valor do produto à vista no dinheiro ou no cheque é igual à {:.0f}R$.'.format(p*0.9))
elif escolha == 2:
    print('O valor do produto à vista no cartão é igual à {:.0f}R$.'.format(p*0.95))
elif escolha == 3:
    print('O valor do produto em até 2x no cartão é igual à {:.0f}R$.')
elif escolha == 4:
    print('O valor do produto em 3x ou mais no cartão é igual à {:.0f}R$.'.format(p*1.2))
print('\033[1;33m{=== FINALIZADO 044 ===}')
