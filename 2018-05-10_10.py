# 打印楼梯，同时在楼梯上方打印两个笑脸
print('\1\1', end='')  # 假装笑脸

for i in range(10):
    for j in range(i):
        print("%c%c" % (219, 219), end='')  # 假装楼梯
    print()