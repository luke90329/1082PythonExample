s = []
for i in range(eval(input())):
    a, b, c, d = map(str,input().split())
    p = (int(b)/1000) + int(c) - int(d)
    s.append([a,int(p)])
for i in range(len(s)):
    for j in range(len(s)):
        if s[i][1] < s[j][1]:
            s[i], s[j] = s[j], s[i]
for i in range(len(s)):
    print(s[i][0], s[i][1])