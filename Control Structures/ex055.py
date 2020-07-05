print('\033[1;33m{=== EXERCÍCIO 055 ===}\033[m')
list = []
for pess in range(1,6):
    peso = float(input(f'\033[1mDigite o peso da {pess}° pessoa: '))
    list += [peso]
print(f'O maior peso foi {max(list):.0f}KG.')
print(f'O menor peso foi {min(list):.0f}KG.')
print('\033[1;33m === FINALIZADO 055 ===')