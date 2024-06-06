#Greatest of three numbers

a=int(input("give number 1:\n"))
b=int(input("give number 2:\n"))
c=int(input("give number 3:\n"))

if (a!=b!=c):
    if (a>b and a>c):
        print(" the greatest of three is {}".format(a))
    elif(b>a and b>c):
        print(" the greatest of three is {}".format(b))
    elif(c>a and c>b):
        print("the greatest of three is {}".format(c))
elif(a==b!=c):
    if(a>c):
        print("greatest of three is {}".format(a))
    elif(c>a):
        print("greatest of three is {}".format(c))

elif(b==c!=a):
    if(a>c):
        print("greatest of three is {}".format(a))
    elif(c>a):
        print("greatest of three is {}".format(c))
elif(c==a!=b):
    if(c>b):
        print("greatest of three is {}".format(c))
    elif(b>c):
        print("greatest of three is {}".format(b))
else:
    print("all the numbers are equal hence {}".format(a))
        
    
    

