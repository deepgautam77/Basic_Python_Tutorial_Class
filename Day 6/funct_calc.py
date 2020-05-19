a=float(input("Enter a first number: "))
b=float(input("Enter a second number: "))
def __adding__(first_input,second_input):
    return first_input+second_input
def sub(first_input,second_input):
    return first_input-second_input
def mul(first_input,second_input):
    return first_input*second_input
def div(first_input,second_input):
    return first_input/second_input
print(round(__adding__(a,b),2))
print(round(sub(a,b),2))
print(round(mul(a,b),2))
print(round(div(a,b),2))

#Write a function called number_of_factors that takes an integer and returns how many factors the number has.

#Write a function called one_away that takes two strings and returns True if the strings are of
# the same length and differ in exactly one letter, like bike/hike or water/wafer.