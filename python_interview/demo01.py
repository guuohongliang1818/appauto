# 姓名：郭宏亮
# 时间：2023/8/21 10:51
print(sum(range(1, 101)))

a = 100


def fn():
    global a
    a = 4


fn()
print("a：", a)
