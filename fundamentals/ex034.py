print('\033[1;33m === EXERCÍCIO 034 === \033[m')
import time
salario = float(input('\033[1mDigite o seu salário:'))
print('\033[1;46m=-=\033[m'*12)
print('\033[1mPARABÉNS, você recebeu um aumento!\033[m')
time.sleep(2)
print('\033[1;46m=-=\033[m'*12)
if salario > 1250:
    print('\033[1mVocê receberá um aumento de 10% no seu salário atual!')
    time.sleep(2)
    print('\033[1mSeu novo salário será de {:.2f}R$!'''.format(salario * 1.10))
else:
    print('\033[1mVocê receberá um aumento de 15% no seu salário atual')
    time.sleep(2)
    print('\033[1mSeu novo salário será de {:.2f}R$!'.format(salario * 1.15))
print('\033[1;33m === FINALIZADO 034 === \033[m')
