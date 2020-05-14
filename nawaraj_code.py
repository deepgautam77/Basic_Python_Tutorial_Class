cont='yes'
while cont=='yes':
    try:
        person_group=['infant','child','adult','senior']
        Ticket_Price=["Your in free category",10,15,12]
        age=int(input('Enter your your age:-'))
        if age<=3 and age>0:
            print(Ticket_Price[0],"Since you are",person_group[0])
        elif age>3 and age<13:
            print("Ticket price is $",Ticket_Price[1], "Since you are", person_group[1])
        elif age>13 and age<59:
            print("Ticket price is $",Ticket_Price[2], "Since you are", person_group[2])
        elif age>60 and age<115:
            print("Ticket price is $",Ticket_Price[3], "Since you are", person_group[3])

        else:
            print("please enter your valid age")
        cont=input("Type 'yes' to continue:-")
    except:
        print("Please Enter valid age between 1-115")