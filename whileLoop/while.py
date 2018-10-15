# for i in range(10):
#     print("i is now {}".format(i))

# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1

# available_exist = ["east", "north east", "south"]
# chosen_exit = ""
#
# while chosen_exit not in available_exist:
#     chosen_exit = input("Please choose a direction:")
#     if chosen_exit == "quit":
#         print("Game Over")
#         break
#
# else: #este codigo solo se ejecuta si no hacemos break en el bucle
#     print("Aren't you glad you got out of there!")

import random

highest = 10
answer = random.randint(1, highest)

print("Please, guess a number between 1 and {}:".format(highest))
guess = 0 #si estamos usando un while necesitamos inicializar la variable primero

# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it!")
#     else:
#         print("Sorry, you have not guessed correctly.")
# else:
#     print("Well done, you got it first try!")

# while guess != answer:
#     guess = int(input())
#     if guess == 0:
#         print("You quit the game")
#         break
#     else:
#         if guess < answer:
#             print("Please guess higher")
#         elif guess > answer:
#             print("Please guess lower")
# else:
#     print("Well done, you guessed it!")


while guess != answer:
    guess = int(input())
    if guess == 0:
        print("You quit the game")
        break
    if guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
    elif guess == answer:
        print("Well done, you guessed it!")
