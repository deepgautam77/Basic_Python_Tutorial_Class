#Convert kg in pounds 1 kg = 2.2 lb
kg = float(input("Enter weight in KG: "))
pnd_1 = (kg * 2.2)
pnd = round(pnd_1,2)
print(f'{kg} kg in pounds is {pnd} lb')     # using f function

print(kg, " kg in pounds is ",pnd," lb.")   #normal way to print strings and declared variables together

print('{} kg in pounds is {}'.format(kg,pnd))   #using .format method
