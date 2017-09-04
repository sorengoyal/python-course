# if-else
# [1]
print('Enter a string:', end = ' ')
s = input()
if s.count('s') != 0:
    output = "Found %d 's'" % (s.count('s'))
else:
    output = "No 's' found"
print(output)

# unpacking
# [1]
date = '09-05-2017'
m,d,y = date.split('-')
print(m,d,y)

# [2]
a = 1
b = 2
a,b = b,a
print(a,b)

#Fun with loops
#[1]
l = [[1,2,3],
    [4,5,6],
    [7,8,9]]
for row in l:
    for elem in row:
        print(elem, end=' ')
    print()

#[2]
a = [1,2,3]
b = [3,4,5]
sum = 0
for (x,y) in zip(a,b):
    sum += x*y
print(sum)
