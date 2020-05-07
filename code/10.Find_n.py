for i in range(eval(input())):  #數學問題需要數學手段
    n = eval(input())
    print(int(n**0.5)+1,end=' ')
    if n**(1/3) == int(n**(1/3)):
        print(int(n**(1/3)) - 1)
    else:
        print(int(n**(1/3)))
