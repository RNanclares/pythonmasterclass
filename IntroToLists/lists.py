# # ipAdress = input("Please enter an IP address:" )
# # print(ipAdress.count("."))
#
# parrot_list = ["non pinin", "no more", "a stiff", "bereft of live"]
# parrot_list.append("A norwegian blue")
# for state in parrot_list:
#     print("This parrot is {}".format(state))
#
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7]
#
# numbers = even + odd
# numbers.sort()
# print(numbers)
#
# print(numbers.sort()) #Retorna None porque el objeto fue mutado
# print(sorted(numbers)) #Retorna la lista ordenada pero es un objeto diferente
#
# numbers_in_order = numbers.sort() #La varia numbers in order es None porque el objeto fue mutado pero no generó un nuevo objeto
# numbers_in_order = sorted(numbers)
# print(numbers_in_order)
#
# numbers = even + odd
#
# if numbers == numbers_in_order:
#     print("The lists are equal")
# else:
#     print("The lists are not equal") #Las listas no son iguales porque no están en el mismo orden
#
# if numbers_in_order == sorted(numbers):
#     print("The lists are equal")
# else:
#     print("The lists are not equal")

#listas vacias

# list_1 = []
# list_2 = list()
#
# print("List 1:{}".format(list_1))
# print("List 2:{}".format(list_2))
#
# if list_1 == list_2:
#     print("Lists are equal")
# else:
#     print("Lists are not equal")
#
# print(list("The lists are equal"))

# even = [2, 4, 6, 8]
#
# another_even = even
# another_even.sort(reverse=True)
#
# print(another_even)
# print(even)
# print(another_even is even) #ambas variables apunta al mismo objeto
#
# another_even = list(even) #creamos un objeto diferente
# another_even.sort(reverse=True)
#
# print(another_even is even)
# print(another_even == even) #ambas listas son iguales


even = [2, 4, 6, 8]
odd = [1, 3, 5, 7]

numbers = [even, odd]
print(numbers)

for number_set in numbers:
    print(number_set)

    for values in number_set:
        print(values)

