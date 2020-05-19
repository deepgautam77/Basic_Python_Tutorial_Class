
#Create a phone directory with name, phone and email. (at least 5)
#WAP to find out all the users whose phone number ends with an 8.
#all the users who doesn't have email address. --done

d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
{'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
{'name':'Princess', 'phone':'555-3841', 'email':''},
{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

#email
#phone that ends with an 8
for item in d:
    if item['email']=='':
        print("The name ",item['name'], "doesn't have email address.")

    if item['phone'].endswith('8'):
        print("The phone number ending at 8: ",item['phone'])

