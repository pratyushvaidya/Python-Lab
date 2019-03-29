class rectangle:
    #normal constructor 
    def __init__(self,len = 0,br = 0):
        self.len = len
        self.br = br
    #function to calculate area
    def calArea(self,rc):
        area = rc.len*rc.br
        print("Area : ",area)

a = rectangle(10,5)
b = rectangle()
#copy constructor call
b.calArea(a)
