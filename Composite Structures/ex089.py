print('\033[1;33m{=== EXERCÍCIO 089 ===}\033[m')
print('\033[1m=-=-=' * 10)
print('{} Boletim com listas compostas'.format(' ' * 12).upper())
print('=-=-=' * 10)
dados = list()
tipo = ''
while True:
    nome = str(input('Digite o Nome do estudante: ')).capitalize().strip()
    n1 = float(input('Digite a 1° Nota: '))
    n2 = float(input('Digite a 2° Nota: '))
    media = (n1 +n2) / 2
    dados.append([nome, [n1, n2], media])
    tipo = input('QUER CONTINUAR? [S/N] ').upper().strip()[0]
    if tipo in 'Nn':
        break
print('=-=' * 10)
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>10}')
for i, n in enumerate(dados):
    print(f'{i:<4}{n[0]:<10}{n[2]:>10.1f}')
print('=-=' * 10)
while True:
    nota = int(input("Mostrar notas de qual Aluno? "
                      "[Pressione 999 para SAIR.] "))
    if nota == 999:
        break
    if nota <= len(dados) - 1:
        print(f'{" " * 5 }Notas de {dados[nota][0]} são {dados[nota][1]} ')
print('\033[1;33m{=== FINALIZADO 089 ===}')
