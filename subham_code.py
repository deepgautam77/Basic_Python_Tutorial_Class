def find_price(age):
    if age<=3:
        print("Free")
    elif (age>3 and age<=12):
        print(" Price: $10")
    elif (age>=13 and age<=59):
        print("Price: $15")
    elif (age>=60):
        print("Price: $12")

num=int(input("How many tickets do you want? "))

for i in range(num):
    user = int(input("Enter your age "))
    find_price(user)
