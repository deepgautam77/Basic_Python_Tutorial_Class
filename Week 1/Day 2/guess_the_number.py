from random import randint
ans=False
while ans==False:
    g_1 = int(input("Player A: Guess your number between 1-10:  "))
    g_2 = int(input("Player B: Guess your number between 1-10:  "))

    x = randint(1,10)
    print(x)

    if x==g_1 and x==g_2:
        print("Both guessed the correct answer.. !!")
    elif x==g_1:
        print("Player A guessed the correct answer.")
        ans=True
    elif x==g_2:
        print("Player B guessed the correct answer.. !!")
        ans=True
    else:
        ans=False