def greatest_prime_factor(num):
	i = 2

	while i * i < num:
		while num % i == 0:
			num = num / i
		i+=1
	return num


print greatest_prime_factor(600851475143)