print('\033[1;33m{=== EXERCÍCIO 040 ===}\033[m')
n1 = float(input('\033[1mDigite a primeira nota do aluno:'))
n2 = float(input('Digite a segunda nota do aluno:'))
media = (n1+n2)/2
if media >= 7:
    print('\033[1;32mVocê está APROVADO, sua média final foi de {:.1f}!'.format(media))
elif 7 > media > 5:
    print('\033[1;33mVocê está de RECUPERAÇÃO, sua média final foi de {:.1f}!'.format(media))
elif media <= 5.0:
    print('\033[1;31mVocê está REPROVADO, sua média final foi de {:.1f}!'.format(media))
print('\033[1;33m{=== FINALIZADO 040 ===}')






