print('\033[1;33m === EXERCÍCIO 018 === \033[m')
from math import radians, sin, cos, tan
ang = float(input('\033[1mDigite um ângulo entre 0° e 360°:'))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('Os valores dos SENO {:.2f}, COSSENO {:.2f} e TANGENTE {:.2f}'.format(sen, cos, tan))
print('\033[1;33m === FINALIZADO 018 ===')

