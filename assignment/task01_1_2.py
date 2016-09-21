# 打印4层金字塔，效果如下
#     *
#    ***
#   *****
#  *******

# 第二种实现方法，原理一样，代码更少

level = 0
while level < 4:
    n = level * 2 + 1  # n 代表* 的个数
    m = 4 - level  # m 代表空格个数
    print(' ' * m + '*' * n)
    level = level + 1
