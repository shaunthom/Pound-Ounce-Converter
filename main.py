m=0
def __init__(self, lb, oz):
    val = lb*16

    total_oz = ((val) + oz)
    lb = total_oz//16
    oz = total_oz % 16
    self.outputs = []
    self.lb = lb
    self.oz = oz
    a=[8,16,24]
    self.a = a

def __str__(self):
    return f"{self.lb} lb {self.oz} oz"

def __add__(self,x):
    
    sum_oz = ((self.lb*self.a[1]) + self.oz ) + ((x.lb*self.a[1])+ x.oz)
    self.outputs.append(sum_oz)
    return Pound(sum_oz//self.a[1], sum_oz%self.a[1])

def __repr__(self):
    return f"Pound({self.lb}, {self.oz})"    

def __sub__(self,y):
    difnce = ((self.lb*self.a[1])+self.oz) - ((y.lb*self.a[1])+y.oz)
    if difnce < self.m:
        raise ValueError
    
    d=difnce%self.a[1]
    if difnce == self.m:
        pass
    return Pound(difnce//self.a[1], d)
