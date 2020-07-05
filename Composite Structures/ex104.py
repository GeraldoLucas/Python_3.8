print('\033[1;33m{=== EXERCÍCIO 104 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{}  Validando entrada de dados em Python'.format(' ' * 6).upper())
print('=-=-=' * 10)


def Leia(num):
    validacao = False
    valor = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            valor = int(n)
            validacao = True
        else:
            print('\033[1;31mERRO! DIGITE UM NÚMERO INTEIRO.\033[m')
            print('\033[1m')
        if validacao:
            break
    return valor


# PROGRAMA PRINCIPAL
n = Leia('Digite um número inteiro: ')
print('Você digitou o número {}.'.format(n))
