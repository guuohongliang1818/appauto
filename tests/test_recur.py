# 姓名：郭宏亮
# 时间：2023/5/30 20:28
def test_recur():
    r = fib(5)
    print(r)


def fib(n):
    if n == 1:
        return 1
    return n * fib(n - 1)
