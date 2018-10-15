# this is a comment

# greeting = 'Hello'
# name = input("Please enter your name:")
# print(greeting + ' ' + name)

# splitstring = "This string has been\nsplit over\nseveral\nlines"
#
# print(splitstring)
#
# tabbedstring = "1\t2\t3\t4\t5\t"
#
# print(tabbedstring)

# print('The pet shop owner said "No, no \'e\'s uh,... he\'s resting"')
# print("The pet shop owner said \"No, no, 'e's uh,...he's resting\"")
#
# anotherSplitString = """This string has been
# split over
# several linves"""
#
# print(anotherSplitString)
#
# print('''The pet shop owner said "No, no, 'es' uh,... he's resting"''')

#variables

# age = 24
# greeting = 'Raul'
#
# print(greeting + ' ' + str(age))
#
# a = 12
# b = 3
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)

#operator precedence, division and modulo first

# print(a + b / 3 -4 *12)
# print(8 / 2 * 3)
# print(8 * 3/2)
# print((((a + b)/3)-4)*12)
#
# c = a + b
# d = c / 3
# e = d - 4
# print(e * 12)

parrot = 'Norwegian Blue'

print(parrot)
print(parrot[0])
print(parrot[3])
print(parrot[-1])
print(parrot[0:6])
print(parrot[:6])
print(parrot[6:])
print(parrot[-4:2]) #doesn't work
print(parrot[-4:-2])
print(parrot[0:6:2])
print(parrot[0:6:3])

number = "9,223,372,036,854,775,807"
print(number[1::4])
numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::2])

string1 = "he's "
string2 = "probably "
print(string1 + string2)
print("he's " "probably " "pining")
print("Hello " *5)
#print("Hello " *5+4)
print("Hello " * (5+4))
print("Hello" * 5 + "4")
today = "friday"
print("day" in today)
print("fri" in today)
print("thur" in today)
print("parrot" in today)