print('\033[1;33m{=== EXERCÍCIO 103 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{}  Função para Ficha do Jogador'.format(' ' * 10).upper())
print('=-=-=' * 10)
from time import sleep


def jogador(nome='<desconhecido>', gols=0):
    return print(f'O jogador {nome} marcou {gols} gol(s) na temporada.')


nome = str(input('Digite o nome do jogador: ')).upper()
gol = str(input('Quantos gols marcou na temporada: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    jogador(gols=gol)
else:
    jogador(nome, gol)

sleep(2)
print('\033[1;33m{=== FINALIZADO 103 ===}')