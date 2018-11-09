
def checkpali(a):
    a = a.lower().replace(' ','')
    if a[::-1] == a:
        print('{} es un palíndromo.'.format(a))
    else:
        print('{} no es un palíndromo.'.format(a))


a = 'Amad a la dama'

checkpali(a)
