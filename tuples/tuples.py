#
# t = 'a', 'b', 'c'
#
# print(t)
#
# print('a', 'b', 'c') #Parametros separados por comas
# print(('a', 'b', 'c')) #Tupla
#

# welcome = 'Welcome to my Nightmare', 'Alice Cooper', 1975
# bad = 'Bad Company', 'Bad Company', 1974
# budgie = 'Nightflight', 'Budgie', 1981
# imelda = 'More mayhem', 'Emilda May', 2011
# metallica = 'Ride the Lightning', 'Metallica', 1984

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
#
# imelda = imelda[0], 'Imelda May', imelda[2]
# print(imelda)

# metallica2 = ['Ride the Lightning', 'Metallica', 1984]
#
# metallica2.append('Rock')
# print(metallica2)
#
#
# title, artist, year = imelda #this is called unpacking the tuple
# print(title)
# print(artist)
# print(year)
#
# title, artist, year = metallica2
# print(title)
# print(artist)
# print(year)

welcome = 'Welcome to my Nightmare', 'Alice Cooper', 1975
bad = 'Bad Company', 'Bad Company', 1974
budgie = 'Nightflight', 'Budgie', 1981
imelda = 'More mayhem', 'Emilda May', 2011, (
    1, 'Pulling the rug', 2, 'Psycho', 3, 'Mayhem', 4, 'Kentish Town waltz'
)

print(imelda)
