times = eval(input())
for _ in range(times):
    num = eval(input())
    sum = 0
    for i in range(1,num//2 + 1):
        if num % i == 0:
            sum += i
    print(sum)
    if num > sum:
        print('Deficit')
    elif num < sum:
        print('Abundant')
    else:
        print('Perfect')