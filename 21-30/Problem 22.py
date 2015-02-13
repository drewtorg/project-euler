f = open('names.txt')

lst = list(f)

names = lst[0].split(',');

names.sort()

count = 1
total = 0

for name in names:
	newname = name.strip('"')
	sum = 0
	for char in newname:
		sum += ord(char) - ord('A') + 1
	total += count * sum
	count += 1

print total



