class MagicCalculator:
    def __init__(self, number_1,number_2):
        self.number_1 = number_1
        self.number_2 = number_2
    def __add__(self, other):
        return self.number_1 + other.number_1, self.number_2 + other.number_2
    def __sub__(self, other):
        return self.number_1 - other.number_1, self.number_2 - other.number_2
    def __mul__(self, other):
        return self.number_1 * other.number_1, self.number_2 * other.number_2
    def __div__(self, other):
        return self.number_1 / other.number_1, self.number_2 / other.number_2
    def __divs__(self, other):
        return self.number_1 // other.number_1, self.number_2 // other.number_2  

num1 = MagicCalculator(8,9)  
num2 = MagicCalculator(7,3) 
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
    
 
        
        
    