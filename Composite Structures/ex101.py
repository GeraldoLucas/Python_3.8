print('\033[1;33m{=== EXERCÍCIO 101 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{} Funções para votação'.format(' ' * 9).upper())
print('=-=-=' * 10)
from time import sleep
import datetime


def votacao(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = (ano_atual - ano)

    print('Sua idade é de {} anos.'.format(idade))
    sleep(2)

    if idade < 16:
        print(f'Com {idade} você NÃO VOTA.')
    elif 16 <= idade < 18:
        print(f'Com {idade} anos seu voto é FACUTATIVO.')
    elif 60 >= idade >= 18:
        print(f'Com {idade} anos seu voto é OBRIGATÓRIO.')
    elif idade > 60:
        print(f'Com {idade} anos seu voto é FACUTATIVO.')


votacao(int(input('Qual o ano de seu nascimento?')))
sleep(2)
print('\033[1;33m{=== FINALIZADO 101 ===}')
