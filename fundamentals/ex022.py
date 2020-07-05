print('\033[1;33m === EXERCÍCIO 022 === \033[m')
nome = input('\033[1mDigite um nome:').strip()
print('Analisando suas informações...')
print('O nome com as letras maiúsculas: {}.'.format(nome.upper()))
print('O nome com as letras minúsculas: {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem ao todo {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele possui {} letras'.format(separa[0], len(separa[0])))
print('\033[1;33m === FINALIZADO 022 ===')






