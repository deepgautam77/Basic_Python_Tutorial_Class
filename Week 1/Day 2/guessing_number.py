from random import randint

ans=False
x= randint(1,10)
while ans== False:

    guess_1 = int(input("Player A, Please guess your number between 1-10:  "))
    guess_2 = int(input("Player B, Please guess your number between 1-10:  "))


    if guess_1 == x and guess_2 == x:
        print("Both of you guessed the correct Number..")

    elif guess_1==x:
        print("Player A guessed the correct answer..")
        ans=True

    elif guess_2==x:
        print("Player B guessed the correct answer..")
        ans = True
    else:
        ans=False