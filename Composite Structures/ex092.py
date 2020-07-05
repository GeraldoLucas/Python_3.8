print('\033[1;33m{=== EXERCÍCIO 092 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{} Cadastro de Trabalhador em Python'.format(' ' * 13).upper())
print('=-=-=' * 10)
import datetime
dados = {}
dados['Nome'] = str(input('Digite seu nome: ')).strip().capitalize()
nasc = int(input('Digite o Ano de Nascimento: '))
dados['Idade'] = datetime.date.today().year - nasc
dados['CTPS'] = int(input('Carteira de Trabalho e Previdência Social [0 Não possui]: '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Digite seu salário: R$ '))
    dados['Aposentadoria'] = 35 + (datetime.date.today().year)
    dados['Idade_Aposentadoria'] = dados['Idade'] + ((dados['Contratação'] + 35) - datetime.date.today().year)
print('=-=-=' * 10)
for k, v in dados.items():
    print(f'{k} = {v}')
print('\033[1;33m{=== FINALIZADO 092 ===}')
