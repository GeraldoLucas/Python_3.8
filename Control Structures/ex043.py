print('\033[1;33m{=== EXERCÍCIO 043 ===}\033[m')
peso = float(input('\033[1mQual é o seu peso, em quilogramas?(KG)'))
alt = float(input('Qual é sua altura, em metros?(m)'))
imc = (peso)/(alt)**(2)
print('=-='*13)
print('-Abaixo de 18.25  : Abaixo do Peso')
print('-Entre 18.25 e 25 : Peso ideal')
print('-Entre 25 e 30    : Sobrepeso')
print('-Entre 30 e 40    : Obesidade')
print('-Acima de 40      : Obesidade Mórbida')
print('=-='*13)
print('\033[1;32mSeu imc é igual a {:.1f}.\033[m'.format(imc))
if imc < 18.25:
    print('\033[1mVocê está ABAIXO DO PESO.')
elif 25 > imc >= 18.25:
    print('\033[1;32mVocê está no PESO IDEAL.')
elif 30 > imc >= 25:
    print('\033[1;31mVocê está com SOBREPESO.')
elif 40 > imc >= 30:
    print('\033[1;31mVocê está com OBESIDADE.')
else:
    print('\033[1;31mVocê está com OBESIDADE MÓRBIDA.')
print('\033[1;33m{=== FINALIZADO 043 ===}')


