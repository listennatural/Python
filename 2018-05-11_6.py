# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
st1 = ' 123 abc !@#  123 abc !@#'
x = 0; y = 0; z = 0; s = 0

for i in range(len(st1)):
    if ord(st1[i]) == 32:
        y += 1
    elif ord(st1[i]) in range(48, 58):
        z += 1
    elif ord(st1[i]) in range(65, 91) or ord(st1[i]) in range(97, 123):
        x += 1
    else:
        s += 1

print('英文字母：', x, ';空格：', y, ';数字：', z, ';其他字符：', s)