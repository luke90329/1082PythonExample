times = eval(input())
for _ in range(times):
    num = eval(input())
    sum = num
    b = ''
    while sum >= 2:           #轉2進制
        b += str(sum % 2)
        sum = (sum-(sum % 2))//2
    b += str(sum)
    if list(b).count('1') % 2 == 0: #判斷1的基偶
        print(f'{num}: YES')
    else:
        print(f'{num}: NO')