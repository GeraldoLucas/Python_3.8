print('\033[1;33m{=== EXERCÍCIO 056 ===}\033[m')
med = 0
velho = 0
nomevelho = 0
mulher = 0
for c in range(1,5):
    print('\033[1m=-=' * 12)
    nome = input('Digite o nome da {}° pessoa: '.format(c))
    idade = int(input('Digite a idade: '))
    sexo = input('Qual o seu sexo [F/M]: ')
    if idade:
        med += (idade / 4)
    if c == 1 and sexo in "Mm":
        velho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > velho:
        velho = idade
        nomevelho = nome
    if mulher < 20 and sexo in 'Ff':
        mulher +=1
print('A média de idade dos participantes é igual à {:.1f} anos.'.format(med))
print(f'O homem mais velho é o {nomevelho}  que tem {velho} anos.')
print('Ao todos {} mulheres têm menos de 20 anos.'.format(mulher))
print('\033[1;33m === FINALIZADO 056 ===')


