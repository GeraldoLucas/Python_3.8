print('\033[1;33m{=== EXERCÍCIO 090 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{}  Dicionário em Python'.format(' ' * 13).upper())
print('=-=-=' * 10)
aluno = dict()
aluno['Nome'] = str(input('Nome do aluno: ')).strip().capitalize()
aluno['Média'] = float(input('Média do aluno: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'APROVADO'
elif 7 > aluno['Média'] >= 6:
    aluno['Situação'] = 'RECUPERAÇÃO'
else:
    aluno['Situação'] = 'REPROVADO'
for k, v in aluno.items():
    print('- ', k, ' =', v)
print('\033[1;33m{=== FINALIZADO 090 ===}')
