print('\033[1;33m{=== EXERCÍCIO 053 ===}\033[m')
f = str(input('\033[1mDigite uma frase:')).upper().strip().split()
junt = ''.join(f)
print(f'Sua frase: {junt}')
print(f'O inverso de sua frase é: {junt[::-1]}')
if junt == junt[::-1]:
    print('\033[1;32mESSA FRASE É UMA PALÍNDROMO!')
else:
    print('\033[1;31mESSA FRASE NÃO É UMA PALÍNDROMO!')
print('\033[1;33m === FINALIZADO 053 ===')
#APOS A SOPA
#A SACADA DA CASA
#A TORRE DA DERROTA
#O LOBO AMA O BOLO
#ANOTARAM A DATA DA MARATOMA