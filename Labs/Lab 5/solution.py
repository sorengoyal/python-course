#Comprehensions
#1
l = []
res = [e for e in dir(l)]

#2
m = [[1,2,3],
    [4,5,6],
    [7,8,9]]

#2
s = [sum(row) for row in m]

#3
m_t = [[row[i] for row in m] for i in range(0,3)]

#Generators
#1
def capitalize(l):
    for word in l:
        yield word[0].upper() + word[1:]
#2
def printer(l):
    for word in l:
        print(word)
        yield len(word)

words = ['spam', 'ham', 'chiclet']
capitals = capitalize(words)
lengths = printer(capitals)
for i in range(0,3):
  print(next(lengths))
