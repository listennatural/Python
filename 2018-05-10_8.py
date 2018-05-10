# 输出九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        x = '  ' if i * j < 10 else ' '
        print(i, '*', j, '=', i * j, end=x)
    print()