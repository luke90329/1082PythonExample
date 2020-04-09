for i in range(eval(input())):
    b = eval(input())
    card = b
    while card >= 3:
        b += card//3
        card = card % 3 + card // 3
    else:
        print(b)
        continue;