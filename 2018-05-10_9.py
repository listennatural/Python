# 要求输出国际象棋棋盘
# 不研究Python图形界面，使用html完成
for i in range(1, 9):
    print('----------------------------------')
    x = '|黑色' if i % 2 == 0 else '|白色'
    y = '|白色' if i % 2 == 0 else '|黑色'
    for j in range(1, 9):
        z = x if j % 2 == 0 else y
        print(z, end='') if j < 8 else print(z, end='|\n')
print('----------------------------------')