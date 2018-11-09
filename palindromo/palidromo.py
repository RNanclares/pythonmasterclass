import re

def checkpali(a):
    regex = re.compile('[^a-zA-Z]')
    b = a
    b = b.lower().replace(' ','')
    b = regex.sub('', b)
    if b[::-1] == b:
        print('{} es un palíndromo.'.format(a))
    else:
        print('{} no es un palíndromo.'.format(a))


a = 'Amad a la dama'

checkpali(a)
