print('\033[1;33m{=== EXERCÍCIO 057 ===}\033[m')
#print(f'O sexo é {s}.')
s = str(input('\033[1mInforme qual é o seu sexo [F/M]? ')).strip().upper()[0]
while s not in 'Ff' and s not in 'Mm':
    s = str(input('Dados inválidos, informe novamente o seu sexo [F/M]: ')).strip().upper()[0]
print(f'O sexo {s} foi registrado com sucesso.')
print('\033[1;33m === FINALIZADO 057 ===')
