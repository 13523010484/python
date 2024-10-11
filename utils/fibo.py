# 斐波那契数列模块

def fib(n):    # 打印斐波那契数列直到 n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # 返回斐波那契数列直到 n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


# 添加下面的代码，这个文件既能被用作脚本，又能被用作一个可供导入的模块
# 在终端运行 python utils/fibo.py 50
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))