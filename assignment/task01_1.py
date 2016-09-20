# 打印4层金字塔，效果如下
#     *
#    ***
#   *****
#  *******

level = 0
line = ''

stars  = '*******************************************'
spaces = '                                           '

while level < 4:
    n = level * 2 + 1       # n 代表* 的个数
    m = 4 - level           # m 代表空格个数

    line = spaces[:m] + stars[:n]
    print(line)

    level = level + 1