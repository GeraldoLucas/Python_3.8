print('\033[1;33m{=== EXERCÍCIO 062 ===}\033[m')
print('\033[1m=-=-=' * 11)
print('{}MONITOR PROGRESSÃO ARITMÉTICA'.format(' ' * 10))
print('=-=-=' * 11)
a = int(input('\033[1mDigite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
termo = a
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}', end=' | ')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('QUANTOS TERMOS VOCÊ DESEJA ADICIONAR? '))
print('=-=-=' * 11)
print('\033[1;33m{=== FINALIZADO 062 ===}')
