#ask user for Name

name=str(input("What is your name? \n"))

#ask user for age

age=str(input("What is your age? \n"))

#ask user for city

city=str(input("Which city do you live in? \n"))
#ask user what they enjoy

joy=str(input("What do you like ? \n"))
#output sentence

#using '+' to concatenate 
print("User's name is  "+name+", user is "+age+" years old. \n User live in"+city+" ,user likes to "+joy+".")

#using format to concatenate
print("User's name is {0}, user is {1} years old.\n User lives in {2}, user like to {3}.".format(name,age,city,joy))
