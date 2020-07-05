print('\033[1;33m === EXERCÍCIO 032 === \033[m')
import datetime
print('\033[1;46m-=-\033[m' * 10)
print('\033[1;36mANO BISSEXTO, LEAP YEAR\033[m')
print('\033[1;46m-=-\033[m' * 10)
ano = int(input('\033[1mDigite o valor de um ano, digite 0 para o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano {} é um ano BISSEXTO, LEAP YEAR.'.format(ano))
else:
    print('O ano {} NÂO é um ano BISSEXTO, LEAP YEAR.'.format(ano))
print('\033[1;33m === FINALIZADO 032 ===\033[m')

