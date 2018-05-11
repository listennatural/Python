# 将一个正整数分解质因数。例如：输入 90,打印出 90=2*3*3*5
x = 71
result = list()

while True:
    for i in range(2, x + 1):
        if x % i == 0:
            x = x / i
            result.append(i)
            break
    print(x)
    if x == 1 or x == x:
        break

print(x if x != result[0] else result[0], '= ', end='')
for i in range(len(result)):
    print(result[i], end=' * ' if i + 1 != len(result) else '')