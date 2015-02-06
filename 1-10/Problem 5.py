def smallest_multiple(nums):
	
	num = 2
	while not are_multiples(num, nums):
		num += 2
	return num

def are_multiples(num, nums):
	for x in nums:
		if num % x != 0:
			return False
	return True

print smallest_multiple(range(1, 21))

#takes about a minute to compute