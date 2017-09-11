print "Hello I'm a program that turns Kilometers in Miles"
newConversion="yes"
while newConversion== "yes":

    kilometers = input("Enter value in kilometers")


    conversion = 0.621371

    # calculate miles
    miles = kilometers * conversion
    print str(kilometers )+ " kilometers "  +  " is "  + str( miles )  + " miles"

    newConversion= raw_input(" do you wanna make a new conversion? Type yes or no")
while newConversion== "no":
    print "Goodbay"
    break




