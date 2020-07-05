print('\033[1;33m{=== EXERCÍCIO 039 ===}\033[m')
import datetime
from datetime import date
n = int(input('\033[1mDigite qual o seu ano de nascimento:'))
ano = date.today().year
idade = (ano - n)
print('Você nasceu no ano de {}, então você tem {} ano(s) em {}.'.format(n, idade, ano))
if (idade) == 18:
    print('\033[1;36mEstá na hora de seu alistamento!\033[m')
elif (idade) > 18:
    print('\033[1;31mVocê passou em {} anos da idade de alistamento!'.format(idade - 18))
    print('SEU ANO DE ALISTAMENTO FOI EM {}.'.format(n + 18))
elif (idade) < 18:
    print('\033[1;31mAinda faltam {} anos para seu alistamento!.'.format(18 - (2020 - n)))
    print('SEU ALISTAMENTO SERÁ EM {}.'.format(n + 18))
print('\033[1;33m{=== FINALIZADO 039 ===}')
