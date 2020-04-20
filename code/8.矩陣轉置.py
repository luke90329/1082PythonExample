for i in range(eval(input())):
    a, b = map(int,input().split())
    s = [[0]*3 for i in range(2)]
    for j in range(a):
        l = input().split()
        for z in range(b):
            s[z][j] = l[z]
    for i in s:
        for j in i:
            print(j,end=' ')
        print()
