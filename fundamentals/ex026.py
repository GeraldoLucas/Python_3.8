print('\033[1;33m === EXERCÍCIO 026 === \033[m')
frase = str(input('\033[1mDigite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareçe na {}º posição'.format(frase.find('A')+1))
print('A última letra A aparece na posição {}º.'.format(frase.rfind('A')))
print('\033[1;33m === FINALIZADO 026 === \033[m')











