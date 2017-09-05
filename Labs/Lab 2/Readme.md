# Lab 2

> For this lab you will need to take input. <br>
> The function `input()` gets input from the user and returns it as a string.

## if-else
1. Take input from a user and check if the string has a 's' in it. The input and output should be as shown in the example.
```
>>> Enter a string: sense
Found 2 's'
```
```
>>> Enter a string: field
No 's' found
```

## Unpacking

1. Consider the standard date format - `'mm-dd-yyyy'`. Break it up into 3 variables `m`, `d` and `y` such that they contain the month, day and year respectively. Use the popular string method `split()` to remove the `-` and get a list of `['mm','dd','yyyy']`. Unpack the list into the vaiables `m`, `d` and `y`.

2. Given two variables `a` and `b` swap their values in one line of code. (*Hint: Use unpacking*)

## Fun with loops

1. Consider the matrix stored as list of lists -
```python
l = [[1,2,3],
    [4,5,6],
    [7,8,9]]
```
Print the matrix above in a 3x3 grid -
```python
1 2 3
4 5 6
7 8 9
```

2. Compute the dot product of two vectors represented as list. Use `zip()` to simultaneously iterate over both the lists.
