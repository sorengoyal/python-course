def shuffle(pairs):
        d = {}
        for (key, value) in pairs:
                if not key in d:
                        d[key] = []
                d[key].append(value)
        return d
data1 = [('hello', 1), ('master', 1), ('hello', 1), ('master', 2)]
data2 = shuffle(data1)
print(data2)
