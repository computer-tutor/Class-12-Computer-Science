def only_if(marks):
    if(marks>90):
        print("You achieved a distinction")
    if(marks>80):
        print("You achieved 80+")
    if(marks>70):
        print("You acheived 70+")


def if_else(marks):
    if(marks>90):
        print("You achieved a distinction")
    else:
        print("You didn't achieve any distinction but <90")


def if_elif_else(marks):
    if (marks>90):
        print("You achieved a distinction")
    elif (marks>70):
        print("You didn't achieve any distinction but 70+")
    elif (marks>80):
        print("You didn't achieve any distinction but 80+")
    else:
        print("You've scored less than 70!")

#Main Program Starts
marks = 86
if_elif_else(marks)
