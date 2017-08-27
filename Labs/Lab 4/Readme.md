# Lab 4

1. Write a function `shuffle` that takes as input a list of key-value pairs and returns groups all values by keys.
A sample run would be -
```python
data1 = [{'hello':1}, {'master':1}, {'hello':1}, {'master':2}]
data2 = shuffle(data1)
print(data2)
```
The output will be -
```python
{hello:[1,1]}, master:[1,2]}
```
Note that the it takes in a list of key-value pairs and returns an dictionary of key value pairs.
