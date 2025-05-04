from ExampleClass import exampleClass
#Classes
#Classes are the most important thing to know
#They have constructors and methods/functions
#The first thing to do with a class is to make sure you import the class from the created file like you can see above
#To create an instance of a class (an object) you make it like a variable but instead of giving it a value you give it the constructor
example1 = exampleClass()
#Some classes have multiple constructors
#The exampleClass made up there is using the default constructors
#This gives it defualt values for its instance variables, and instance variable is a variable tied to a specific object
#However the class exampleClass has another constructor where you choose what the instance variables are set to
example2 = exampleClass(4536,True,"The Minutebots")
#Once you have an instance of a class it may use the functions of the class
example1.changeStr("Just in time")
example1.exampleMutator(6354)
example2.exampleFunc()
#In order to create a class you must first right class className:
#Then everything that is indented will be in the class
#To make the constructor you use the syntax def __init__(self,): and you add any variables you want the constructor to take in after the self and sepperated by commas
#To make functions you write def funcName(self,): and add any wanted variables like in the constructor
#All of this syntax can be seen in the file ExampleClass.py
#Look there for more information and examples


#Can you make a new file called car.py
#In that file make a class called car
#It will have 2 constructors, one is a default constructor that initialises the variables miles to -1, gasInTank to -1, model to "Not Applicable", and brand to "Not Applicable"
#The other constructor will take in a float to set miles, an int to set gasInTank, and 2 strings to set model and brand
#The car class will have a function to add an int to gasInTank up to a max of of 100
#The class will also have a function called getInfo to print the variables miles, gasInTank, model, and brand







#After you make your car class you should look through the code for the robot from the most recent season