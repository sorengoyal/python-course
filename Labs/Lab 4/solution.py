#Lab 4
#singletonSet
def singletonSet(n):
    return lambda x: x == n

#union
def union(s, t):
    return lambda n: s(n) or t(n)

# intersect
def intersect(s, t):
    return lambda n: s(n) and t(n)

#diff
def diff(s, t):
    return lambda n: s(n) and not t(n)

#filter
def filter(s, p):
    return lambda n: s(n) and p(n)

#forall
def forall(s, p):
    n = -100
    while n <= 100 :
        if s(n) and not p(n) :
            return False
        n = n + 1
    return True
#exists
def exists(s, p):
    return not forall(s, lambda x: not p(x))
#map
def map(s, f):
    return lambda n: exists(s, lambda x:f(x) == n)

#Sample code
a = singletonSet(10)
b = singletonSet(20)
c = singletonSet(23)
ab = union(a, b)
abc = union(ab, c)
p = lambda x: x in [10,20]

print(str(forall(ab, p)))
print(str(exists(abc, p)))
abc_twice = map(abc, lambda x: 2*x)
print(str(abc_twice(40)))
