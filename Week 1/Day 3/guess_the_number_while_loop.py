from random import randint

sec_num = randint(1,10)
g_1 = 0
while g_1 != sec_num:
    g_1 = eval(input("Players, Please guess the number:  "))

print(sec_num)
print("You finally got it.")