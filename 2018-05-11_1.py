"""
古典问题：
    有一对兔子，从出生后第 3 个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？满足 斐波那契数列
"""
count = 1  # 雌雄成对数目
count1 = 1
count2 = 1

for month in range(1, 13):
    x = '第%d个月有%d只兔子'
    if month in [1, 2]:
        print(x % (month, 2))
    else:  # 当前月份所有兔子的数量是前两个月份兔子数量之和
        count1 = count2
        count2 = count
        count = count1 + count2
        print(x % (month, count * 2))