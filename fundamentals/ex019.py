print('\033[1;33m === EXERCÍCIO 019 === \033[m')
import random
a = input('\033[1mPrimeiro aluno:')
b = input('Segundo aluno:')
c = input('Terceiro aluno:')
d = input('Quarto aluno:')
membros = [a, b, c, d]
escolhido = random.choice(membros)
print('O aluno escolhido foi {}'.format(escolhido))
print('\033[1;33m === FINALIZADO 019 ===')




