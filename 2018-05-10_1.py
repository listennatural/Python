# 有 1,2,3,4 四个数字，能组成多少个互不相同且无重复的数字？都是多少？
st = '1234'
set1 = set()

for i in st:

    for j in st:
        set1.add(int(i + j))

print(set1, len(set1))