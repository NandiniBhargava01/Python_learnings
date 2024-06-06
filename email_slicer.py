#email slicer



#ask user for email address

email=input("enter your email:\n").strip()

#seprate the user name from the email using slice and storing that in a new variable

user_name=email[:email.index('@')]

#seprate the domain name from the email using slice and storing that in a new variable

domain_name=email[email.index('@') +1:]

#create a output that we want to display

output="Your user name is \' {1} \' and your domain name is\' {0} \' ".format(domain_name,user_name)

#print the desired output
print(output)

