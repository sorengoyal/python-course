Use the existing code in lab.py.

Part1
=====
The code has a list of 10 numbers that is being sorted using selection sort. However, the code is incorrectly written. Correct the code. (Code has errors in two lines only)

*About selection sort*
The Selection Sort algorithm is the simplest example of a sorting algorithm.  A sorting algorithm takes a list of items and returns them in sorted order.  Selection sort performs this action by searching through the list for the smallest value in the list, swapping it with the first item in the list.  It then repeats this process (swapping the second elements of the list with the second smallest, the third element with the third smallest, etc.) until the entire list has been sorted.

A very simple version of the algorithm for selection sort is as follows:
1. Set the current index to 0
2. Loop over the entire list from the current index to the end, searching for the minimum value
3. Swap the mimum value with the value at the current index
4. Increment the current index by 1 and repeat from step 2 until the current index is the final position of the list

Part 2
======

Instead of sorting 10 numbers, we will sort 100,000 numbers. For this write extra code to create list of 100,000 random numbers. Use the code that you wrote for sorting to sort this list. You will need to modify the loop to make it run 100,000 times.

