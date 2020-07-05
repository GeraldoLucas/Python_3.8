print('\033[1;33m{=== EXERCÍCIO 095 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{} Aprimorando os Dicionários'.format(' ' * 13).upper())
print('=-=-=' * 10)
dados = dict()
lista = list()
cont = 0
while True:
    dados['Jogador'] = str(input('Nome do Jogador: ')).strip().capitalize()
    dados['Partidas'] = int(input(f'Quantas partidas {dados["Jogador"]} jogou? '))
    if dados["Partidas"] != 0:
        for c in range(0, dados['Partidas'] ):
            dados['Gols'] = int(input(f' - Gols na {c+1}° partida: '))
            lista.append(dados['Gols'])
            cont += dados['Gols']
    tipo = str(input('Quer continuar? [S/N] ')).strip().upper().split()[0]
    if tipo in 'Nn':
        break
    if tipo not in 'Ss':
        print('     ERRO     ')
        tipo = str(input('Novamente. Quer continuar? [S/N] ')).strip().upper().split()[0]
print('=-=-=' * 8)
print('Cód     Nome       Gols       Total')
for i,  in enumerate(lista):
    print(f'{i+1}° partida: {p} gols.')
print('\033[1;33m{=== FINALIZADO 095 ===}')



