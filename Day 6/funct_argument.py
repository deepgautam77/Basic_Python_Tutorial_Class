#arguments are important in function

#1) positional 2) keywords 3) default values

def person(name, email):
    print("My name is ", name)
    print("My email is ", email)

person('DG','dg@python.com')

def personal_details(name, email, phone):
    print("My name is ",name)
    print("My email is ", email)
    print('My phone no. is ',phone)

personal_details(email="dk@python.org", phone='6825524827', name='NIrvaya GAutam')

#default values

def details(name, sex='male'):
    print("The person name is ",name)
    print("The person sex is ", sex)

details("Harry")
details("Radha", sex='Female')