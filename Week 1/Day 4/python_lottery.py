#WAP to generate six different lucky numbers for a lottery program and allow user to input their 6 digit lottery number.
#Match if the person won the lottery or not. lottery number should be between 1-48.

from random import randint, choice, sample, shuffle
L = [randint(1,48) for i in range(6)]
print(L)

add=0

user_lottery_number = []
for i in range(6):
    num=int(input("Enter your lucky number simultaneously: "))
    user_lottery_number.append(num)
print(user_lottery_number)

for i in range(len(L)):
    if L[i] in user_lottery_number:
        add+=1
    else:
        print("You didn't win the lottery.")
        break
if add==6:
    print('You won the lottery.')

#WAP
#infant (age 0-3) free tickets
#child ticket (age 3-12) $10.00
#adult ticket (age 13-59) $15
#senior citizen ticket (age>60) $12
#let user enter their age. Give the price of ticket according to the cinema hall rules.