def validate_distinction(marks):
    if marks>90:
        return marks
    else:
        pass

#Main Program Starts    
name = input("Enter your name:")
marks = 91
tuition = "Computer Tutor"
distinction = validate_distinction(marks)
if distinction:
    print("You've distinction because you studied from ", tuition)
else:
    print("You don't have distinction because you didn't study from Computer Tutor.")
