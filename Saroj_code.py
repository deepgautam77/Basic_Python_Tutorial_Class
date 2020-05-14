
price = []

number = input("Enter the total number of ticket you wanted: ")
num = 1
while num <= int(number):
    age = int(input(f"Enter the age of the person: "))
    num +=1
    if age in range(4):
        price.append(0)
    elif age in range(4, 13):
        price.append(10)
    elif age in range(13, 60):
        price.append(15)
    else:
        price.append(12)

print("")
print("Total Amount = $",sum(price))