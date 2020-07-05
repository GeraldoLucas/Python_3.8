print('\033[1;33m === EXERCÍCIO 011 \033[m===')
larg = float(input('\033[1mQual a largura da parede?'))
alt = float(input('Qual a altura da parede?'))
area = (larg * alt)
print('A parede tem a  dimensão de {:.2f}m x {:.2f}m e sua área total é {:.0f}m²'.format(larg, alt, area))
print('Sabendo que cada litro tinta pinta um equivalente a 2m².\nEntão são necessários {:^.1f}L tinta'.format(area/2))
print('\033[1;33m === FINALIZADO 011 \033[m===')

