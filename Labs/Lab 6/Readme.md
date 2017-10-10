# Lab 6

In this this lab we create a simple class MyComplex to handle complex numbers.
Sample code using the class will look like this -
```python
c = MyComplex(1,2)
d = MyComplex(3,4)
print(c+d)
print(abs(c))
print(c == d)
```
## Modules
1. Start by creating a module called `mycomplex`.
2. Create a the class `MyComplex` inside the module `mycomplex`.
3. Add two member variables -
  1. real
  2. imag
4. Implement the `__repr__` method to print the complex number in its proper form.
5. Implement the methods for adding, checking equality and computing absolute value. (*Hint: Introspect the python's built-in `complex` object using `dir()` to discover the methods that need to be implemented*)
6. Add the sample code inside the module as described in Slide
