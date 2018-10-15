# for i in range(1, 20):
#     print("i is now {}".format(i))
#
# number = "9,223,372,036,854,775,807"
#
# for i in range(0, len(number)):
#     print(number[i])

# number = "9,223,372,036,854,775,807"
# cleanedNumber = ''
#
# for i in range(0, len(number)):
#     if number[i].isdigit():
#         cleanedNumber = cleanedNumber + number[i]
#         #print(number[i], end='')
#
# newNumber = int(cleanedNumber)  # type: int
# print("The number is {}".format(newNumber))

# number = "9,223,372,036,854,775,807"
# cleanedNumber = ''
#
# for char in number:
#     if char.isdigit():
#         cleanedNumber = cleanedNumber + char
#
# newNumber = int(cleanedNumber)  # type: int
# print("The number is {}".format(newNumber))

# for state in ["not pinin", "no more", "a stiff", "bereft of lift"]:
#      print("This parrot is " + state)

# for i in range(0, 100, 5):
#     print("i is {}".format(i))

# for i in range(1, 13):
#     for j in range(1, 13):
#         print("{1} times {0} is {2}".format(i, j, i*j), end='\t')
#     print("")

quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.

for char in quote:
    if char in 'ABCDEFGHIJKLMNOPQRSTUWXYZ':
        print(char, end=' ')

