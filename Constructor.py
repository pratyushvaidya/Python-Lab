class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.img = i

c1 = ComplexNumber(2,3)
print(c1.real, c1.img)

c2 = ComplexNumber()
print(c2.real, c2.img)
