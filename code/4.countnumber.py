for i in range(eval(input())):
    a = eval(input())
    sum = 0
    while a > 0:
        sum += 1 / a
        a -= 1
    print(sum)
