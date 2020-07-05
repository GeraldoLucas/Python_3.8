print('\033[1;33m{=== EXERCÍCIO 041 ===}\033[m')
import datetime
from datetime import date
nasc = int(input('\033[1mQual o ano de seu nascimento?'))
atual = date.today().year
idade = atual - nasc
print('Você nasceu em {}, então você tem {} anos em {}.'.format(nasc, idade, atual))
if idade <= 9:
    print('Categoria: MIRIM')
elif 14 >= idade > 9:
    print('Categoria: INFANTIL')
elif 19 >= idade >14:
    print('Categoria: JUNIOR')
elif 25 >= idade > 19:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')
print('\033[1;33m{=== FINALIZADO 041 ===}\033[m')