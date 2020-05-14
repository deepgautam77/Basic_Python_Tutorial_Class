price = {
    'infant':'Free', 'child':10, 'adult':15, 'senior':12
}
print(price)

age=int(input("Enter your age: "))
ans=False
while ans==False:
    while age>0 and age<101 and ans==False:

        if age>0 and age<4:
            print(price['infant'])
            ans = True

        elif age>3 and age<13:
            print(price['child'])
            ans = True

        elif age>12 and age<60:
            print(price['adult'])
            ans = True

        elif age>59 and age<101:
            print(price['senior'])
            ans=True
    else:
        print("Enter valid age between 1-100.")

        age= int(input("Enter your age: "))