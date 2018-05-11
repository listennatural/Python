# 判断 101-200 之间有多少个素数，并输出所有素数
set1 = set()

for i in range(101, 201):
    status = True
    for j in range(2, i):
        if i % j == 0:
            status = False
            break
    if status:
        set1.add(i)

print(set1, '总共%d个素数' % len(set1))