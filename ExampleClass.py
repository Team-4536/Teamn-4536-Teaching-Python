class example:
    def __init__(self):
        self.var1 = 0
        self.var2 = False
        self.var3 = "Hello"


    def __init__(self, v1: int, v2: bool, v3: str):
        self.var1 = v1
        self.var2 = v2
        self.var3 = v3


    def exampleFunc(self):
        if(self.var2):
            self.var2 = False
            print(self.var1)
        else:
            self.var2 = True
            print(self.var3)


    def exampleMutator(self, b: int):
        self.var1 = b
    
    def changeStr(self, b: str):
        self.var3 = b
