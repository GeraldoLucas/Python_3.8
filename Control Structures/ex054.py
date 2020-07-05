print('\033[1;33m{=== EXERCÍCIO 054 ===}\033[m')
import datetime
ano = datetime.date.today().year
menor = 0
maior = 0
for n in range(1,8):
    idade = int(input(('\033[1mDigite o ano de nascimento da {}° pessoa:'.format(n))))
    if (ano - idade) < 21:
        menor += 1
    elif (ano - idade) >= 21:
        maior += 1
print(f'Ao todo {menor} pessoas são menores de idade.')
print(f'E ao mesmo tempo {maior} pessoas são maiores de idade.')
print('\033[1;33m === FINALIZADO 054 === ')
