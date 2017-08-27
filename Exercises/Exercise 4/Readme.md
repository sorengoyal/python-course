# Exercise 4
> Based on Assignments of "Functional Programming Principles of Scala" Course by Martin Odersky

## Functional Sets

In this exercise we will represent sets using Function objects.

### Introduction

As an example to motivate our representation, how would you represent the set of all negative integers? You cannot list them all. One way would be so say: if you give me an integer, I can tell you whether it’s in the set or not: for 3, I say ‘no’; for -1, I say yes.

Mathematically, we call the function which takes an integer as argument and which returns a boolean indicating whether the given integer belongs to a set, the characteristic function of the set. For example, we can characterize the set of negative integers by the characteristic function `lambda x: x < 0`.

Therefore, we choose to represent a set by its characteristic function and define a type alias for this representation:

### Basic Set Functions
Let’s start by implementing basic functions on sets.

1. Define a function singletonSet which creates a singleton set from one integer value: the set represents the set of the one given element. Now that we have a way to create singleton sets, we want to define a function that allow us to build bigger sets from smaller ones.

2. Define the functions union,intersect, and diff, which takes two sets, and return, respectively, their union, intersection and differences. diff(s, t) returns a set which contains all the elements of the set s that are not in the set t.

3. Define the function filter which selects only the elements of a set that are accepted by a given predicate p. The filtered elements are returned as a new set.

### Queries and Transformations on Sets

In this part, we are interested in functions used to make requests on elements of a set. The first function tests whether a given predicate is true for all elements of the set. This `forall` function has the following signature:
```python
def forall(s: 'Set', p: 'lambda int->boolean')-> boolean
```
Note that there is no direct way to find which elements are in a set. contains only allows to know whether a given element is included. Thus, if we wish to do something to all elements of a set, then we have to iterate over all integers, testing each time whether it is included in the set, and if so, to do something with it. Here, we consider that an integer x has the property -1000 <= x <= 1000 in order to limit the search space.

1. Implement `forall` using linear recursion. For this, use a helper function nested in `forall`. (Remember function are just objects in Python they can be declared anywhere)

2. Using `forall`, implement a function `exists` which tests whether a set contains at least one element for which the given predicate is true.

3. Finally, write a function map which transforms a given set into another one by applying to each of its elements the given function.

### Hints

> 1. Sets are represented as functions. Think about what it means for an element to belong to a set, in terms of function evaluation. For example, how do you represent a set that contains all numbers between 1 and 100?

> 2. Most of the solutions for this assignment can be written as one-liners. If you have more, you probably need to rethink your solution. In other words, this assignment needs more thinking than coding.
