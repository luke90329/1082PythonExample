for i in range(eval(input())):
    a, b = map(int,input().split())
    s = [[0]*a for i in range(b)]
    for j in range(a):
        l = input().split()
        for z in range(b):
            s[z][j] = l[z]
    for i in s:
        print(*i)