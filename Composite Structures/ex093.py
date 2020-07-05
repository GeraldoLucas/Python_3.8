print('\033[1;33m{=== EXERCÍCIO 093 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{} Cadastro de Jogador de Futebol'.format(' ' * 13).upper())
print('=-=-=' * 10)
dados = dict()
cont = 0
lista = list()
dados['Jogador'] = str(input('Nome do Jogador: ')).strip().capitalize()
dados['Partidas'] = int(input(f'Quantas partidas {dados["Jogador"]} jogou? '))
if dados['Partidas'] != 0:
    for c in range(1, dados['Partidas']+1):
        gols = int(input(f'Gols na {c}° Partida: '))
        lista.append(gols)
        cont += gols
dados['Total_Gols'] = cont
print('=-=-=' * 10)
print(f'O jogador {dados["Jogador"]} jogou {dados["Partidas"]} partidas.')
for k, p in enumerate(lista):
    print(f' - Na {k+1}° partida marcou {p} gols.')
print('{} marcou no total {} gols.'.format(dados["Jogador"], dados["Total_Gols"]))
print('\033[1;33m{=== FINALIZADO 093 ===}')