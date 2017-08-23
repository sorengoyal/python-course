# Exercise 1

## [1] Install Python
Go to [www.python.org](www.python.org) and download Python version 3.6.2. Follow the instructions on the website to install it.

> For this course we will not use any IDE. But if you are looking for some good ones I recommend [PyCharm](https://www.jetbrains.com/pycharm/) and [Spyder](https://pythonhosted.org/spyder/)

## [2] Run a Hello World Program

Create a file *hello.py*. With the following contents
```python
 print("Hello World")
```
 Execute the code by typing in the following line in **Terminal** (on Mac and Linux) or **Command Prompt** (on Windows)
 ```bash
  $ python hello.py
 ```


# [3] Correct the code
Use the code in the file *sort.py.*
The code has a list of 10 numbers that is being sorted using selection sort. However, the code is incorrectly written. Correct the code. (Hint: Code has errors in two lines only)

**About selection sort** <br>
 The Selection Sort algorithm is the simplest example of a sorting algorithm.  A sorting algorithm takes a list of items and returns them in sorted order.

 A very simple version of the algorithm for selection sort is as follows:
  1. Set the current index to 0
  2. Loop over the entire list from the current index to the end, searching for the minimum value
  3. Swap the minimum value with the value at the current index
  4. Increment the current index by 1 and repeat from step 2 until the current index is the final position of the list

The algorithm can be understood as follows. It starts by searching through the list for the smallest value in the list, swapping it with the first item in the list.  It then repeats this process (swapping the second elements of the list with the second smallest, the third element with the third smallest, etc.) until the entire list has been sorted.

 # [4] Extend the code

 Instead of sorting 10 numbers, we will sort 100,000 numbers. For this write extra code to create list of 100,000 random numbers. Use the code that you wrote for sorting to sort this list. You will need to modify the loop to make it run 100,000 times.

 > *Note*: Although the we will cover the for loops in detail later, for this exercise simple for-loops should work
