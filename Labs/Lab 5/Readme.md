# Lab 5

## Comprehensions
1. Given a list `l=[]`, print the output of `dir(l)` neatly,i.e one element per line. Use a comprehension expression to achieve this.

Given a matrix m, arranged by rows -
```python
m = [[1,2,3],
    [4,5,6],
    [7.8.9]]
```
2. Write a comprehension expression to find the sum of elements of each row.

3. Write a another expression to compute the transpose of the matrix. The result should look as follows -
```python
m_t = [[1,4,7],
      [2,5,8],
      [3,6,9]]
```
## Generators
We will create a pipeline to perform computation on a lists.
We begin with a simple list of words -
```python
words = ['spam', 'ham', 'chiclet']
```

1. Write a generator function `capitalize()` that accepts the list and capitalizes the first letter of each word.
> 'upper()' method of present in string object will be useful

2. Write a another generator function `printer` that takes a list as argument. For each word in the list it prints the word and returns the length of the word.

The following code will use the functions you just created.
```python
capitals = capitalize(words)
lengths = printer(capitals)
for i in range(0,3):
  print(next(lengths))
```
 Run this code and make sure that the output matches the following
 ```python
Spam
4
Ham
3
Chiclet
7
 ```
