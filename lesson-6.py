# 方式一、导入整个包
import utils.fibo as fibo
print('方式一：导入整个包')
print('fibo.fib::',fibo.fib(100))
print('fibo.fib2::',fibo.fib2(100))

# 方式二、导入来个各个模块的方法名
from utils.fibo import fib, fib2
print('方式二、导入来个各个模块的方法名')
print('fib.::',fib(100))
print('fib2::',fib2(100))

# 方式三、导入模块内定义的所有名称
from utils.fibo import *
print('方式三、导入模块内定义的所有名称')
print('fib.::',fib(100))
print('fib2::',fib2(100))


# 模块搜索路径
import sys

# 打印模块搜索路径
print("Current module search path:")
for path in sys.path:
    print("path::",path)

print('# 添加新的路径到搜索路径')
# 添加新的路径到搜索路径
new_path = '/path/to/new/directory'
sys.path.append(new_path)

# 再次打印模块搜索路径，验证新路径是否已添加
print("\nUpdated module search path after adding new directory:")
for path in sys.path:
    print(path)


import sys
print(sys.path)


# dir 函数
import utils.fibo, sys
print('dir::',dir(utils.fibo))
print('sys::',dir(sys))

