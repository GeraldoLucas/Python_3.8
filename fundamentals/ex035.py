print('\033[1;33m=== EXERCÍCIO 035 ===\033[m')
a = float(input('\033[1mDigite o comprimento da primeira régua: '))
b = float(input('Digite o comprimento da segunda régua: '))
c = float(input('Digite o comprimento da terceira régua: '))
ce = abs(b-c) < a < (b+c) and \
abs(a-c) < b < (a+c) and \
abs(a-b) < c < (a+b)
if ce:
    print('Essas três réguas formam um Triângulo!')
    if a == b == c:
        print('Essas três réguas formam um triângulo Equilátero!')
    if a == b != c or a == c != b or b == c != a:
        print('Essas três réguas formam um triângulo Isósceles!')
else:
    print('Essas três réguas não formam um triângulo!')
print('\033[1;33m === FINALIZADO 035 === \033[m')



