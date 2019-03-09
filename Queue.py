class queue:
    List=[]
    len=0
    def add(self,x):
        self.List.append(x)
    def print(self):
        print(self.List)
    def delete(self):
        print("Removed: ",self.List[0])
        self.List.remove(self.List[0])
        
c1 = queue()

c1.add(5)
c1.add(6)
c1.add(2)
c1.print()

c1.delete()
c1.print()
