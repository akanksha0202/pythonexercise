shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
    if item == 'spam':
        print("I am ignoring " + item)
        continue
    print("Buy " + item)

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
    if item == 'spam':
        print("I am ignoring " + item)
        break
    print("Buy " + item)

meal = ["egg", "bacon", "spam", "sausages"]

nasty_food_item = ''
for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
if nasty_food_item == 'spam':
    print("\n Can't I have anything without spam in it")

meal = ["egg", "bacon", "spam", "sausages"]
nasty_food_item = ''

for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break
else:
    print("i'll have a plate of that, then, please")

if nasty_food_item == 'spam':
    print("\nCan't I have anything without spam in it")
