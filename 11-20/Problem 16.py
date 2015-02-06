def power_sum(n):
	power = 2 ** n
	lst = [int(x) for x in str(power)]
	return sum(lst)

print power_sum(1000)