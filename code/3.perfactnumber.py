for i in range(eval(input())):
    a = eval(input())
    s = []
    sum = 0
    for j in range(1,a):
        if a % j == 0:
            sum += j
    if sum == a:
        print('True')
    else:
        print('False')
    