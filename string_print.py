from random import randint
my_list = []
for i in range(1,11):
    my_num = randint(50,100)
    my_list.append(my_num)
print(my_list)

even=0
odd=0
for i in range(len(my_list)):
    if i%2==0:
        even+=1
    else:
        odd+=1

print("The total even number is ", even)
print("The total odd number is ", odd)