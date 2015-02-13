sum = 0

for i in xrange(1,1001):
	sum += i ** i

string = str(sum)
output = ''
for i in xrange(-10, 0):
	output += string[i]

print output