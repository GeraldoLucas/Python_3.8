print('\033[1;33m{=== EXERCÍCIO 073 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{} Tuplas com Times de Futebol'.format(' ' * 11).upper())
print('=-=-=' * 10)
times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
         'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará',
         'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
g5 = (times[0], times[1], times[3], times[4], times[5])
rebaixamento = (times[16], times[17], times[18], times[19])
print('{}LIBERTADORES'.format(' ' * 14))
for pos, equipe in enumerate(g5):
    print('{}° colocação {}'.format(pos + 1, equipe))
print('=-=-=' * 10)
print('{}REBAIXAMENTO'.format(' ' * 14))
for pos, equipe in enumerate(rebaixamento):
    print('{}° colocação {}'.format(pos + 17, equipe))
print('=-=-=' * 10)
print('{}ORDEM ALFABÉTICA'.format(' ' * 14))
for list in sorted(times):
    print(list)
print(f'A {times[18]} terminou em {times.index("Chapecoense")}° posição no Brasileirão 2019.'.upper())
print('\033[1;33m{=== FINALIZADO 073 ===}')

