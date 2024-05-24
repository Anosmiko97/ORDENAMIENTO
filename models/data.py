class dataElement:
    def __init__(self):
        self.data10 = case()
        self.data100 = case()
        self.data1000 = case()
        self.name = ""
        
    # Getter y Setters
    def getData10(self):
        return self.data10
    def setData10(self, data):
        self.data10 = data
        
    def getData100(self):
        return self.data100
    def setData100(self, data):
        self.data100 = data
        
    def getData1000(self):
        return self.data1000
    def setData1000(self, data):
        self.data1000 = data
        
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
        
class case:
    def __init__(self):
        self.better_case = None
        self.average_case = None
        self.worse_case = None
        
    #Getters y Setters
    def getBetterCase(self):
        return self.better_case
    def setBetterCase(self, case):
        self.better_case = case
    
    def getAverageCase(self):
        return self.average_case
    def setAverageCase(self, case):
        self.average_case = case
        
    def getWorseCase(self):
        return self.worse_case
    def setWorseCase(self, case):
        self.worse_case = case

    def setAllAttributes(self, b, a, w):
        self.better_case = b
        self.average_case = a
        self.worse_case = w
            