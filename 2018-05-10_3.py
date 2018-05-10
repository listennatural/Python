# 一个整数，它加上 100 后是一个完全平方数，再加上 168 又是一个完全平方数，请问该数是多少？
import math

i = 0

while True:
    i1 = math.sqrt(i + 100)
    if str(i1).split('.')[1] == '0':
        i2 = math.sqrt(i + 268)
        if str(i2).split('.')[1] == '0':
            print(i)
            break

    i += 1