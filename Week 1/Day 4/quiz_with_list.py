questions = ["What is the capital city of Nepal? ", "National bird of Nepal ","Height of Sagarmatha "]
answers = ["Kathmandu", "Danfe", "8848"]

num_right = 0
for i in range(len(questions)):
    guess=(input(questions[i]))
    if guess.lower()==answers[i].lower():
        print("Correct")
        num_right = num_right + 1
    else:
        print("Wrong answer !! :@ ")
        print("You have ", num_right," right answer.")