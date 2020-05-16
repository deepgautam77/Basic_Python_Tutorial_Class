res_menu_items = {
    'samosa': 9.99,
    'chowmein': 15.99,
    'momo': 19.99,
    'ice cream': 5.99,
    'burger': 14.99
}

ordered_items = {
    'chicken chilli',
    'samosa',
    'ice cream',
    'burger'
}

total = 0
for item in ordered_items:
    item=item.lower()
    if item in res_menu_items:
        print('{}: {}'.format(item, res_menu_items[item]))
        #print(item, ':', res_menu_items[item])
        total += res_menu_items[item]
    else:
        print("Sorry, we do not have your order of ",item)
print("-"*20)
print('Order Total: {}'.format(total))