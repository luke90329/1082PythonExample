a, b = map(int,input().split())
for i in range(a):
	s = list(input())
	for j in s:
		c = (ord(j) - b - 97)
		if c < 0:
			c += 26
		print(chr(c + 97),end='') 
	print()