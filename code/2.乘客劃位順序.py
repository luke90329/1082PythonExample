s = []
for i in range(eval(input())):
    a, b, c, d = map(str,input().split())
    p = (int(b)/1000) + int(c) - int(d)
    s.append((a,int(p)))
s.sort(key=lambda x:x[1])
for i in range(len(s)):
    print(s[i][0], s[i][1])