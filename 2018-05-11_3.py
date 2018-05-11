"""
打印出所有的“水仙花数” ，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。例如： 153 是一个“水仙花数” ，因为 153=1 的三次方＋5 的三次方＋3 的三次方
"""
li1 = list()

for i in range(100, 1000):
    x = int(str(i)[0])
    y = int(str(i)[1])
    z = int(str(i)[2])

    if pow(x, 3) + pow(y, 3) + pow(z, 3) == i:
        li1.append(i)

print(li1)