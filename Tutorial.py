#So this is how you put python codes and run!
# First we are going to make a password contained in a variable!


x="hello"
#hello is my password.

y=raw_input("What is your Username:")
#raw_inout is basically prompting a user to answer a question.

if y=="Pranav" or y=="pranav":
    print("Hello Pranav!")
    d=raw_input("What is your password Pranav:")
    if d==x:
        print ("Welcome back Pranav!!")
    else:
        while not d==x:
            print("Help!! I am being Hacked!!")
            d=raw_input("What is your password Pranav:")
            if d==x:
                print ("Welcome back Pranav!!")

else:
    while not y=="Pranav" and (not y=="pranav"):
        print "I dont know you!"
        y=raw_input("What is your Username:")


if y=="Pranav" or y=="pranav":
    print("Hello Pranav!")
    d=raw_input("What is your password Pranav:")
    if d==x:
        print ("Welcome back Pranav!!")
    else:
        while not d==x:
            print("Help!! I am being Hacked!!")
            d=raw_input("What is your password Pranav:")
            if d==x:
                print ("Welcome back Pranav!!")


#So this is the code to make an authentication system.

#and means that both the conditions should be true!

                #Now lets run it.
