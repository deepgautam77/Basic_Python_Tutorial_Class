
def number_of_factor(num):
    times = 0
    for i in range(1, num+1):
        rem = num % i
        if rem == 0:
            times += 1
            print(i, end=" ")
    return times


def one_away(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    if len1 == len2:
        times = 0
        for i in range(len1):
            if str2[i] != str1[i]:
                times += 1
        if times == 1:
            return True
        else:
            return False
    else:
        return False



number = int(input("Enter a number whose total numbers of factors is to be determined: "))
print(f"\nThe factors of the integer {number} are: ")
factor = number_of_factor(number)
print(f"\nThe total number of factor of the integer {number} is {factor}.")

word_1 = input("\nEnter a word: ")
word_2 = input("Enter another word: ")

check = one_away(word_1.title(), word_2.title())
if check:
    print(f"\n{word_1.title()} and {word_2.title()} are two words of equal length having same letters except for one.")
else:
    print(f"\n{word_1.title()} and {word_2.title()} are two very different words.")
