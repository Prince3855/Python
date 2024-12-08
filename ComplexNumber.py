"""
Create complex number class with operator support
"""

class ComplexNumber:
    def __init__(self, real=0.0, imaginary=0.0):
        self.real = real
        self.imaginary = imaginary
    
    def __str__(self):
        if self.imaginary == 0.0:
            return f"{self.real}"
        if self.imaginary < 0:
            return f"{self.real} - {abs(self.imaginary)}i"
        return f"{self.real} + {self.imaginary}i"
    
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)
    
    def __mul__(self, other):
        real = self.real * other.real - self.imaginary * other.imaginary
        imaginary = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real, imaginary)
    
    def __truediv__(self, other):
        denominator = other.real**2 + other.imaginary**2
        real = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return ComplexNumber(real, imaginary)
    
    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary
    

c1 = ComplexNumber(3,4)
c2 = ComplexNumber(3,4)

print(c1 == c2)