import random
#In order to make something happen only sometimes you can use an if statement
#The syntax for an if statement is if(boolean): and then everything that is indented after it will be in the if statment
number = 4
if(number < 10):
    print("This ran because number was less than 10")

#If statements can be expanded using elif to make another if statement that can only run if the original if statement doesnt run
#Else statements goes at the end and is what runs if nothing else did
#Example
if(number > 5):
    print("This always gets checked first")
elif(number == 4):
    print("This works as another if statement that might not run")
    print("It ran here because number was 4 meaning the first if statement was false")
else:
    print("This will always run if the rest of the if statement is false")


#Your turn
#Using if, elif, and else make a statement that prints Opuhala if testNum is greater than 7, prints Cassiopeia if testNum is between 3 and 7 and Flymer for any other value
testNum = random.randint(1,10)



#If you want to make something happen if 2 or more things are true using and allows you to connect them
#Using or causes the if statement to happen if one of the things is true
#Example
var1 = random.randint(1,2)
var2 = random.randint(1,2)
if(var1 == 1 and var2 == 1): #Checks if both are true
    print("var1 and var2 were 1")
elif(var1 == 1 or var2 == 1): #Checks if one is true
    print("var1 or var2 was equal to 1")
else:
    print("Neither var1 or var2 equalled 1")

#You can practice that if you want but you just need to remember it