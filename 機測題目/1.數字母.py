times = eval(input())
for _ in range(times):
	string = input().split()
	count = 0
	for i in string:
		if len(i) >= 10:
			count += 1
	print(count)
