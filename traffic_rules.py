#According to the colour of traffic light tell the user what to do

print("Welcome to Traffic rules \n")
light=input("Enter the traffic light you see:\n")

#user can give values in upper case or lower case therefore we need to give one format 
if (light.lower()=="green"):
    print("GO")
elif(light.lower()=="red"):
    print("STOP")
elif(light.lower()=="yellow"):
    print("WAIT")
else:
    print("Light is broken")
