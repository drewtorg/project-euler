def build_digit_string(limit):
	digits = ''
	i = 1
	while len(digits) < limit:
		digits += str(i)
		i += 1
	return digits

def solve():
	
	digits = build_digit_string(1000000)
	offset = 1
	product = 1
	for i in [1,10,100,1000,10000,100000,1000000]:
		product *= int(digits[i - offset])
	return product

print solve()
