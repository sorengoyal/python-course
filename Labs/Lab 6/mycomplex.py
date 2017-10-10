from math import sqrt
class MyComplex:
    def __init__(self, a, b):
        self.real = a
        self.imag = b
    def __add__(self, c):
        return MyComplex(self.real + c.real, self.imag+c.imag)
    def __sub__(self, c):
        return MyComplex(self.real - c.real, self.imag-c.imag)
    def __abs__(self):
        return sqrt(self.real**2 + self.imag**2)
    def __repr__(self):
        return "%f + i%f" %(self.real, self.imag)
    def __eq__(self, c):
        return self.real == c.real and self.imag == c.imag

if __name__ == '__main__':
    c = MyComplex(1,2)
    d = MyComplex(3,4)
    print(c+d)
    print(abs(c))
    print(c == d)
