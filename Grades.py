#Grading students based on marks

#marks>=90 grade="A"
#90>marks>=80,grdae="B"
#80>marks>=70,grade="C"
#70>marks,grade="D"

print("\t \t Grade based on marks obtained \n")
marks=int(input("Enter the marks obtained:\t "))
if(marks<0 or marks>100):
    print("Incorrect value added")
elif(marks>=90):
    print("Grade is A")
elif(marks<90 and marks>=80):
    print("Grade is B")
elif(marks<80 and marks>=70):
    print("Grade is C")
else:
    print("Grade is D")

