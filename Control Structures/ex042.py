print('\033[1;33m{=== EXERCÍCIO 042 ===}\033[m')
a = float(input('\033[1mDigite o comprimento da primeira régua:'))
b = float(input('Digite o comprimento da segunda régua:'))
c = float(input('Digite o comprimento da terceira régua:'))
ce =  abs(b-c) < a < abs(b+c) and abs(a-c) < b < abs(a+c) and abs(a-b) < c < abs(a+b)
if ce:
    print('\033[1;32mEssas três réguas FORMAM um triângulo ', end ='')
    if a==b!=c or a==c!=b or b==c!=a:
        print('\033[1;32mISÓSCELES!')
    elif a==b==c:
        print('\033[1;32mEQUILÁTERO!')
    elif a!=b!=c:
        print('\033[1;32mESCALENO!')
else:
    print('\033[1;31mEssas três réguas NÃO FORMAM um triângulo!\033[m')
print('\033[1;33m{=== FINALIZADO 042 ===}')