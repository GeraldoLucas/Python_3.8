print('\033[1;33m === EXERCÍCIO 020 === \033[m')
from random import sample
a = input('\033[1mNome do primeiro aluno:')
b = input('Nome do segundo aluno:')
c = input('Nome do terceiro aluno:')
d = input('Nome do quarto aluno:')
lista = [a, b, c, d]
ordem = sample(lista, k=3)
print('A ordem de escolha é:')
print(ordem)
print('\033[1;33m === FINALIZADO 020 ===')






