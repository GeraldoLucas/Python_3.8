print('\033[1;33m{=== EXERCÍCIO 059 ===}\033[m')
import time
n1 = int(input('\033[1mInforme o 1° número inteiro: '))
n2 = int(input('Informe o 2° número inteiro: '))
esc = 0
while esc != 5:
      print('|=-=-=-=-=-=-=-= MENU =-=-=-=-=-=-=-=|\n'
            '[ 1 ]  SOMAR\n'
            '[ 2 ]  MULTIPLICAR\n'
            '[ 3 ]  MAIOR\n'
            '[ 4 ]  NOVOS NÚMEROS\n'
            '[ 5 ]  SAIR DO MENU  ')
      print('|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|')
      esc = int(input('Escolha uma das opções do menu: '))
      if esc == 1:
            s = n1+n2
            print('O resultado da soma é igual à {}.'.format(s))
      elif esc == 2:
            m = n1 * n2
            print('O resultado da multiplicação é igual à {}.'.format(m))
      elif esc == 3:
            if n1 > n2:
                  print('O primeiro valor {} é maior que o segundo valor {}.'.format(n1, n2))
            elif n2 > n1:
                  print('O segundo valor {} é maior que o primeiro valor {}.'.format(n2, n1))
            else:
                  print('Os dois valores são iguais ({}).'.format(n1))
      elif esc == 4:
            print('ESCOLHA NOVAMENTE SUAS OPÇÔES!')
            n1 = int(input('Informe o 1° número inteiro: '))
            n2 = int(input('Informe o 2° número inteiro: '))
      else:
            print('Opção inválida, tente novamente!')
      time.sleep(4)
print('MENU FINALIZADO, Volte sempre!')
print('\033[1;33m === FINALIZADO 059 ===')
