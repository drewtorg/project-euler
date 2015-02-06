fibSum = 0
fib = 2
fib2 = 1

while fib < 4000000:
	if fib % 2 == 0:
		fibSum += fib
	temp = fib
	fib += fib2
	fib2 = temp

print fibSum