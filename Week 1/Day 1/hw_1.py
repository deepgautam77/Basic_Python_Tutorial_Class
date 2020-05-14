menu_items = {
    'fries': 15.00,
    'steak': 14.00,
    'egg': 9.00,
    'rice': 12.00,
    'pizza': 23.00,
    'chicken' : 15.99
}

customer_order = []
active = True
prompt = "\nPlease enter an item you want to order:"
prompt += "\n(Enter 'done' when you are finished.) "

while active:
    input_order = input(prompt)
    if input_order.lower() == 'done':
        active = False
    else: customer_order.append(input_order)
Total=0
print("\nYour Orders are : ")
for item in customer_order:
    if item in menu_items:
        print('{} : ${}'.format(item,menu_items[item]))
        Total += menu_items[item]
    else:
        print("sorry, we don't have {}".format(item))
print("----------------")
print("Total : $" + str(round(Total,2)))