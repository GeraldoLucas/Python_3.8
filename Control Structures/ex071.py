print('\033[1;33m{=== EXERCÍCIO 071 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{}Simulador de Caixa Eletrônico'.format(' ' * 12).upper())
print('=-=-=' * 10)
din = float(input('Qual valor você deseja sacar? '))
total = din
ced = 50
n = 0
while True:
    if total >= ced:
        total -= ced
        n += 1
    else:
        if n > 0:
            print('Foi debitado {} notas de R${:.0f}.'.format(n, ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        n = 0
        if total == 0: break
print('\033[1;33m{=== FINALIZADO 071 ===}')
