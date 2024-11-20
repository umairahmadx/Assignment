num = [1, 2, 3, 4, 2, 3, 1, 5, 4, 6, 7]
di = {}
use = []

for i in num:
    if i not in use:
        di[i] = 1
        use.append(i)
    else:
        di[i] += 1

print(di)
