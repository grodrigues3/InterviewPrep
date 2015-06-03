import math

global digits
digits = []
def getPermutation(values,n, k):
	global digits
	if values == []:
		return
	n1Fact = 1
	for i in range(1,n):
		n1Fact *= i
	firstDig = values[int(math.ceil(k*1. / n1Fact))-1]
	print firstDig
	values.remove(firstDig)
	digits += [firstDig]
	getPermutation(values,n-1, k%n1Fact)


values = range(1,4)
i = 3
getPermutation(values,3, i)
print digits

