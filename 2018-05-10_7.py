# 输出特殊图案，请在 c 环境中运行，看一看， Very Beautiful!

a = bytes(176); b = bytes(219)
print("%c%c%c%c%c\n", b, a, a, a, b)
print("%c%c%c%c%c\n", a, b, a, b, a)
print("%c%c%c%c%c\n", a, a, b, a, a)
print("%c%c%c%c%c\n", a, b, a, b, a)
print("%c%c%c%c%c\n", b, a, a, a, b)