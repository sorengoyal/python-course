# Dictionaries

# [1]
names = ['melon', 'mango', 'banana', 'apple']
costs = [1.29, 2.55, 0.79, 1.49]
d = dict(zip(names,costs))

# [2]
d['kiwi'] = 3.19

# [3]
d.pop('mango')

# [4]
'strawberry' in d

# [5]
for key in d:
    if d[key] == 2.55:
        print('Exists')


# Sets

# [1]
s = set([2,3,5,7,11,13])

# [2]
s = set('python')

# [3]
set('silent') == set('listen')

# [4]
len(set('mississippi'))


# Files and Lists

# [1]
f = open('names.txt', 'w')
for name in names:
    f.write(name + '\n')
f.close()
