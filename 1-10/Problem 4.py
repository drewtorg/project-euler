def is_palindrome(string):
	min = 0
	max = len(string) - 1
	while min < max:
		if string[min] != string[max]:
			return False
		min += 1
		max -= 1
	return True

def largest_palindrome_product(nums):
	max = 0
	for i in nums:
		for j in nums:
			if is_palindrome(str(i*j)) and i*j > max:
				max =  i * j
	return max

print largest_palindrome_product(range(100, 1000))
