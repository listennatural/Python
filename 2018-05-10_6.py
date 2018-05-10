# 用 *号输出字母 C的图案。


def fun(x):
    y = ''

    if x < 0:
        return
    else:
        for i in range(x):
            y += ' '
        print(y, '**')


for i in range(1, 15):
    if i < 10:
        fun(10 - 2 * i)
    else:
        fun(2 * (i - 10))