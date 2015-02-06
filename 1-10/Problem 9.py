def is_pythagorean_triplet(a,b,c):
	return (a ** 2 + b ** 2) == c ** 2

def is_special_triplet(a,b,c):
	return (a + b + c) == 1000

def answer():
	for c in range(1,1000):
		for b in range(1,c):
			for a in range(1,b):
				if is_pythagorean_triplet(a,b,c) and is_special_triplet(a,b,c):
					print str(a) + ' ' + str(b) + ' ' + str(c)
					return a * b * c

print answer()