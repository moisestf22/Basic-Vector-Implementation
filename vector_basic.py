# Author @moisestf22  
import math
import random
from unittest import result

class Vector():
    def __init__(self, dim, rand = False):
        if rand:
            self.items=[]
            for i in range(0,dim):
                self.items.append(random.randint(0,10))
        else: 
            self.items = [0]*dim
    
    def len(self): 
        return len(self.items)
    
    def getitem(self, i):
        if i<0 or i>self.len():
            print("Erroneous dimensions")
            return False
        else:
            result = self.items[i]
            return result

    def isEmpty(self):
        return len(self) == 0

    def setitem(self, i, newValue):
        if (i > self.len()):
            print("Error. Index exceeds array dimension")
            return 
        else:
            self.items[i-1] = newValue


        
    def str(self):
        result = '('
        for i in range(0, self.len()):
            result += str(self.items[i]) + ','
        
        result = result[0:len(result)-1] 

        result += ')'

        return result


    def add(self,other):
        # Adds up the two input vectors
        if(self.len() != other.len()):
            # If their sizes are not equal we cannot
            # they wont be equal
            print("Dimensions are not equal. ")
            return False
        else:
            result = Vector(len(self))
            result.items = [self.items + other.items]

    def eq(self, other):
        # Check whether the two vectors are equal or not
        if (self.len() != other.len()):
            print("The dimensions are different, they're diff.")
            return False
        else: 
            for i in range(0, self.len()):
                if self.items[i] != other.items[i]:
                    print("They are not equal")
                    return False   

    def dot(self, other): 
        # It calculates the dot product of two given vectors
        if (self.len()!=other.len()):
            print('Sizes dont match')
            return False
        else: 
            result = 0
            for i in range(0, self.len()):
                result += self.items[i]*other.items[i]

            return result
            
# TEST YOUR PROGRAM
    
v1 = Vector(5) 
v2 = Vector(5,True) 

v1.setitem(1,2)
v1.setitem(2,8)
v1.setitem(5,-3)
print(v1.items)
print(v2.items)

print(v1.dot(v2))

print('\n',v1.str())


print(v2.len())


