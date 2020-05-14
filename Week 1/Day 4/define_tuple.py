from random import randint, choice, sample, shuffle

#randint == generates random number
#choice == picks a random item from list
#sample == picks a group of random items from the list
#shuffle == shuffles the items of list

list_1 = [1,2,3,4,5,6,7]

print(choice(list_1))

print(sample(list_1,4))

shuffle(list_1)
print(list_1)

#WAP to generate six different lucky numbers for a lottery program and allow user to input their 6 digit lottery number.
#Match if the person won the lottery or not. lottery number should be between 1-48.
