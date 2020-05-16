res_menu_items = {
    'samosa': 9.99,
    'chowmein': 15.99,
    'momo': 19.99,
    'ice cream': 5.99,
    'burger': 14.99
}
customer_order = []
active = True

prompt = "Please enter your order name \n"
prompt += "Please enter 'done' when you finished ordering: "

while active:
    input_order = input(prompt)
    if input_order.lower() == 'done':
        active = False
    else:
        customer_order.append(input_order)
Total=0
print("Your orders are: ")
for item in customer_order:
    if item in res_menu_items:
        print("{}:{}".format(item, res_menu_items[item]))
        Total+=res_menu_items[item]
    else:
        print("Sorry, we do not have your order of {}".format(item))
print('-'*40)
print("Total: ", Total)

#Create a phone directory with name, phone and email. (at least 5)
#WAP to find out all the users whose phone number ends with an 8.
#all the users who doesn't have email address.