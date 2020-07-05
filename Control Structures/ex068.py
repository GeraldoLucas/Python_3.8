print('\033[1;33m{=== EXERCÍCIO 068 ===}\033[m')
from random import randint
print('\033[1m=-=-=' * 10)
print('{}JOGO DO PAR OU ÍMPAR'.format(' ' * 15))
print('=-=-=' * 10)
v = 0
while True:
    n = int(input('Escolha um número inteiro de 0 a 10:'))
    c = randint(0, 10)
    soma = n + c
    tipo = ' '
    while tipo not in 'PI':
        tipo = input('QUAL VOCÊ ESCOLHE PAR OU ÍMPAR [P/I]?').upper().strip()[0]
        print('Você escolheu {} e o computador {}, total de {}.'.format(n, c, soma))
        print('DEU PAR!' if soma % 2 == 0 else 'DEU ÍMPAR!')
    if tipo == 'P':
        if soma % 2 == 0:
            print('PARABÉNS! VOCÊ VENCEU!')
            v += 1
        else:
            print('Você perdeu, tente novamente!')
            break
    if tipo == 'I':
        if soma % 2 != 0:
            print('PARABÉNS! VOCÊ VENCEU!')
            v += 1
        else:
            print('Você perdeu, tente novamente!')
            break
    print('=-=-=' * 10)
print('=-= FIM DE JOGO =-=')
print(f'VOCÊ VENCEU {v} VEZ!' if v == 1 else f'VOCÊ VENCEU {v} VEZES!')
print('\033[1;33m{=== FINALIZADO 068 ===}')
