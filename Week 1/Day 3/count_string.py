#.replace(x)
#print index of letter a for every occurance

text_given = "I am a the one"

length = len(text_given)

for i in range(length):
    for x in text_given:
        if x=='a':
            print(i)