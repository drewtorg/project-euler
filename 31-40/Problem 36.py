def is_palindrome(string):
	min = 0
	max = len(string) - 1
	while min < max:
		if string[min] != string[max]:
			return False
		min += 1
		max -= 1
	return True

def is_double_base_palindrome(num):
	if is_palindrome(str(num)) and is_palindrome(str(bin(num)[2:])):
		return True
	return False

def sum_of_double_palindromes(limit):
	sum = 0
	for i in xrange(1, limit):
		if is_double_base_palindrome(i):
			sum += i
	return sum

print sum_of_double_palindromes(1000000)