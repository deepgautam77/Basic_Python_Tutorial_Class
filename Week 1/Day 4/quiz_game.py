questions = ['Height of Sagarmatha: ', 'Corona virus starting country: ', 'Nepal National Game:', 'Capital City of Nepal: ']
answers = ['8848', 'china', 'Volley Ball', 'Kathmandu']

num_right = 0

for i in range(len(questions)):
    guess = input(questions[i])
    if guess.lower() == answers[i].lower():
        print("Correct!!!")
        num_right+=1
    else:
        print("Your got it wrong. :@ ")
        print("The right answer is ",answers[i])
print("Your total correct answer is ", num_right,'''/''',len(questions))