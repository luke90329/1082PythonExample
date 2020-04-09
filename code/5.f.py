for i in range(eval(input())):
    a = eval(input())
    total = 0
    for i in range(1,a+1):
        sum = 1
        for j in range(1,i+1):
            sum *= j
        total += sum
    print(total)