print('\033[1;33m{=== EXERCÍCIO 037 ===}\033[m')
import math
num = int(input('\033[1mPor favor, digite um número inteiro:'))
print('''De acordo com o número {:.0f}, escolha uma base de conversão númerica:\033[m
\033[1;31m[ 1 ] Sistema BINÁRIO. 
\033[1;34m[ 2 ] Sistema OCTAL. 
\033[1;33m[ 3 ] Sistema HEXADECIMAL.\033[m'''.format(num))
escolha = int(input('\033[1mSelecione uma opção:'))
if escolha == 1:
    print('O número {} convertido em BINÁRIO é igual a {}.'.format(num, bin(num)[2:])) #0b
elif escolha == 2:
    print('O número {} convertido em OCTAL é igual a {}.'.format(num, oct(num)[2:])) #0o
elif escolha == 3:
    print('O número {} convertido em HEXADECIMAL é igual a {}.'.format(num, hex(num)[2:])) #0x
else:
    print('Opção inválida. Tente novamente!')
print('\033[1;33m{=== FINALIZADO 037 ===} ')
