class exampleClass:
    #This is the defualt constructor
    def __init__(self):
        #Generally many variables will have self. added to them
        self.var1 = 0
        self.var2 = False
        self.var3 = "Hello"

    #This is the constructor that takes in parameters
    def __init__(self, v1: int, v2: bool, v3: str):
        #Each parameter that it takes in creates basically a temporary variable that will cease to exist after the function ends
        #That is true for functions as well as the constructor
        self.var1 = v1
        self.var2 = v2
        self.var3 = v3

    #This is how functions are made
    def exampleFunc(self):
        if(self.var2):
            self.var2 = False
            print(self.var1)
        else:
            self.var2 = True
            print(self.var3)

    #Functions can take parameters
    def exampleMutator(self, b: int):
        self.var1 = b
    
    def changeStr(self, b: str):
        self.var3 = b
