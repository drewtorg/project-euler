from math import factorial

def sum_factorial(num):
	fac = factorial(num)
	string = str(fac)
	sum = 0
	for i in string:
		sum += int(i)
	return sum

print sum_factorial(100)