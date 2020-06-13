s = [int(x) for x in input().split()[1::]] #將輸入資料的第一筆去除  [4,2,9,13,21] -----> [2,9,13,21]
s = sorted(s)
sum = 0
for i in range(1,len(s)): #將每一筆等於前面一筆資料和自身相加 [2,9,13,21] -----> [2,11,13,21] ------> [2,11,24,21]
    s[i] = s[i-1] + s[i]
    sum += s[i]
print(sum)