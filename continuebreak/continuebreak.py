# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
#     if item == 'spam':
#         print("I'm ignoring " + item)
#         continue #salta el elemento de la lista
#
#     print("Buy " + item)

meal = ["egg", "bacon", "beans", "sausages"] #cambiar spam por beans
nasty_food_item = ''
for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
else:
    print("I'll have a plate of that, then, please")

if nasty_food_item:
    print("can't i have anything without spam in it")
