#Write a small program to ask for a name and an age,
#  When both values have been entered, check if the person
# is the right age to go on a 18-30 holiday (they must be over 18 and under 31).
# if they are, welcome them to the holiday, otherwise print
# a (polite) message refusing them entry.

name = input("Hi, What's your name?")
age = int(input("How old are you {}?".format(name)))

if 17 < age < 31:
    print("{}, welcome to the holiday!".format(name))
else:
    print("Sorry {}, you're not allowed in this holiday".format(name))