#dictionary:
ticket_sys = {
    'infant':None,
    'child':10,
    'adult':15,
    'senior':12
}
print(ticket_sys)

user_age = int(input("Enter your age: "))

if user_age<4 and user_age>0:
    print("You belong to infant category and Your ticket price is $",ticket_sys['infant'])

elif user_age<13 and user_age>3:
    print(ticket_sys['child'])
elif user_age<60 and user_age>12:
    print((ticket_sys['adult']))
elif user_age<100 and user_age>59:
    print(ticket_sys['senior'])
else:
    print('Please enter the age range between 1-100')