s = [int(x) for x in input().split()]
sum = 0
for i in range(s[0]):
    sum += s[i+1] * s[i+1+s[0]]
print(sum)