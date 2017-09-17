# Exercise 4

1. Write a function `shuffle` that takes as input a list of key-value pairs and groups all values by keys. It should accept a list of 2-tuples and should return a dictionary with each value being a list.
Example of a sample run -
```python
data1 = [{'hello':1}, {'master':1}, {'hello':1}, {'master':2}]
data2 = shuffle(data1)
print(data2)
```
The output will be -
```python
{ hello:[1,1] , master:[1,2] }
```
