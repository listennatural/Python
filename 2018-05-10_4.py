# 输入某年某月某日，判断这一天是这一年的第几天？
# date = input('请输入正确的年-月-日')
date = '2018-02-08'
date_list = date.split('-')
count = 0


def fun(x):
    for i in range(1, int(date_list[1])):
        global count
        if i in [1, 3, 5, 7, 8, 10, 12]:
            count += 31
        elif i == 2:
            count += (29 if x else 28)
        else:
            count += 30


if date_list[0][2:] == '00' and int(date_list[0]) % 400 == 0:
    fun(True)
elif int(date_list[0]) % 4 == 0 and int(date_list[0]) % 100 != 0:
    fun(True)
else:
    fun(False)


print(count + int(date_list[2]))