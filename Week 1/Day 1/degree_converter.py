#Convert Celsius to Farenheit

t= float(input("Enter temp in celsius: "))
f=(9/5*t) + 32
print("The temperature in Farenheit is ",f)

boil_point = 212
fz_point = 32

#if else statement

if f<fz_point:
    print("The temperature is below freezing point.")
elif f>boil_point:
    print("The temperature is above boiling point.")
else:
    print("The temperature is normal.")

#WAP that asks the user for a weight in kg & converts it to pounds (1KG = 2.2 Pounds). If weight is below 120 pounds,
#ask user to take protein, or if weight is above 180 pounds, ask user to loose weight.


