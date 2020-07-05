print('\033[1;33m{=== EXERCÍCIO 093 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{} Unindo dicionários e listas'.format(' ' * 13).upper())
print('=-=-=' * 10)
dados = dict()
acima = dict()
cont = 0
media = 0
mulher = []
while True:
    dados['Nome'] = str(input('Digite o nome: ')).strip().capitalize()
    dados['Sexo'] = str(input('Digite o sexo [M/F]: ')).strip().upper().split()[0]
    if dados['Sexo'] in 'Ff':
        mulher.append(dados['Nome'])
    if dados['Sexo'] not in 'MmFf':
        print(f'{" "* 5}ERRO!')
        dados['Sexo'] = str(input('Digite novamente sexo [M/F]: ')).strip().upper().split()[0]
    dados['Idade'] = int(input('Digite a idade: '))
    tipo = str(input('     Quer continuar? [S/N]')).strip().upper().split()[0]
    cont += 1
    media += dados['Idade']
    if tipo in 'Nn':
        break
    if tipo not in 'Ss':
        print(f'{" "* 5}ERRO!')
        tipo = str(input('Novamente. Quer continuar? [S/N]')).strip().upper().split()[0]
print(f'A) Ao todo tem-se {cont} pessoas cadastradas.')
print(f'B) A média de idade é { media / cont:.1f} anos.')
print(f'C) As mulheres cadastradas foram {mulher}.')
print(f'D) Lista de pessoas que estão acima da média: ')
if dados["Idade"] > media / cont:
    for k, v in dados.items():
        print(f' - {k} = {v}')
print('\033[1;33m{=== FINALIZADO 094 ===}')


