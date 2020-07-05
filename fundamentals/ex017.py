print('\033[1;33m === EXERCÍCIO 017 === \033[m')
from math import hypot
a = float(input('\033[1mDigite o cateto oposto do triângulo retângulo:'))
b = float(input('Digite o cateto adjacente:'))
hip = hypot(a, b)
print('A hipotenusa do triângulo retângulo é igual a: {:.2f}'.format(hip))
print('\033[1;33m === FINALIZADO 017 ===')

