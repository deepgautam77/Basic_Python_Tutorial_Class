from random import randint
#using only while loop
sec_num = randint(1,10)
g_1=0
L=[]
while g_1 != sec_num:
    g_1 = eval(input("Enter your guessed number:  "))
    L.append(g_1)
print(" The secret number is ",sec_num)
print("You finally got it!!!")
print(L)