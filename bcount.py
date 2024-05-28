s=input()
digits_count={'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
for char in s:
	if char.isdigit():
		digits_count[char]+=1
for digit, count in digits_count.items():
	print(count, end = ' ')


