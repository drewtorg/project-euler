def sum_of_squares(num):
	sum = 0
	for i in range(1, num + 1):
		sum += i ** 2
	return sum

def sum_of_numbers(num):
	sum = 0
	for i in range(1, num + 1):
		sum += i
	return sum

x = sum_of_squares(100)
y = sum_of_numbers(100) ** 2
print y - x
