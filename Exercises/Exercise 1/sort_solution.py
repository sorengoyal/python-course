l = [10, 9, 8, 7, 1, 5, 4, 3, 2, 6]

for index in range(0, 10):
	minIndex = index
	for j in range(index, 10):
		if(l[minIndex] >  l[j]):
			minIndex = j
	temp = l[index]
	l[index] = l[minIndex]
	l[minIndex] = temp
print(l[:10])
