print('\033[1;33m{=== EXERCÍCIO 069 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{}ANÁLISE DE DADOS DO GRUPO'.format(' ' * 13))
print('=-=-=' * 10)
cont = 0
tot18 = 0
homem = mulher = 0
mulher18 = 0
while True:
    print('{}CADASTRE UMA PESSOA'.format(' ' * 16))
    idade = int(input('Informe a idade: '))
    if idade >18 :
        tot18 += 1
    sexo = str(input('Informe o sexo [F/M]: ')).upper().strip()[0]
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff':
        mulher += 1
    if sexo in 'Ff' and idade < 18:
        mulher18 += 1
    tipo = str(input('QUER CONTINUAR [S/N]: ')).upper().strip()[0]
    cont += 1
    if tipo in 'Nn':
        break
print('Há {} pessoas cadastradas no grupo!'.format(cont))
print('Há {} pessoas com mais de 18 anos'.format(tot18))
print('Ao todo temos {} homens no cadastro.'.format(homem))
print('Por fim há {} mulheres sendo {} dessas com menos de 18 anos.'.format(mulher, mulher18))
print('\033[1;33m{=== EXERCÍCIO 069 ===}')


