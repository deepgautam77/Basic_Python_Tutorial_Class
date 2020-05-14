from random import randint, sample, shuffle, choice
list_int = [1,2,3,4,5]

list_1 = []

list_1 = list_int[:]

print(list_1)

del(list_int[3])
print(list_int)

#insert
list_int.insert(1,8)
print(list_int)

#WAP that generates 50 random numbers between 1 and 100 and print that number.
L = [randint(1,100) for i in range(50)]
print(L)
print(sample(L,4))
print(choice(L))
shuffle(L)
print(L)