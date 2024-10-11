year = 2016
event = 'Referendum'
# f 相当于 js 中的 $
print(f'Result of the {year} {event}')

# 字符串格式化
yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))


# str
print('--------------str--------------------')
s = 'Hello, world.'
# 适合人读的
print('str::',str(s))
# repr 适合解释器读的
print('repr::',repr(s))
print('str(1/7)::',str(1/7))


x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)


# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = str(hello)
hellos1 = repr(hello)
print('hellos::',hellos,'hellos1::',hellos)

# The argument to repr() may be any Python object:
print(repr((x, y, ('spam', 'eggs'))))

import math
print(f'The value of pi is approximately {math.pi:.9f}.') # 圆周率

# 在 ':' 后传递整数，为该字段设置最小字符宽度，常用于列对齐：
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name,phone in table.items():
    print(f'{name:10} {phone:10d}')


print('------------------------')
animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}.')

print('--------- = 说明符可被用于将一个表达式扩展为表达式文本、等号再加表达式求值结果的形式。---------------')
bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')


print('# 字符串的 format 方法')
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                   other='Georg'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

print('--------------------')
table2 = {k: str(v) for k, v in vars().items()}
message = " ".join([f'{k}: ' + '{' + k +'};' for k in table2.keys()])
print(message.format(**table2))


print('------------------------------')
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))



print('------------手动格式化-------------')
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # 请注意上一行中 'end' 的使用
    print(repr(x*x*x).rjust(4))


print('-------------------------------')
print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))

print('-------------------------------')
import math
print('The value of pi is approximately %5.3f.' % math.pi)

print('-------------------------------')
# 使用 'w' 模式打开文件，如果文件不存在则创建新文件
with open('test_file.txt', 'w', encoding='utf-8') as file:
    # 向文件中写入一些文本
    file.write("这是一个测试文件。\n")
    file.write("这里有一些额外的行。\n")


# 使用 'r' 模式打开文件，只读模式
with open('test_file.txt', 'r', encoding='utf-8') as file:
    # 读取文件的所有内容
    content = file.read()
    # 打印文件内容
    print(content)

print('---------------------------')
from datetime import datetime

# 获取当前日期和时间
current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 追加模式 ('a') 打开文件，写入数据
with open('test_file2.txt', 'a', encoding='utf-8') as f:
    f.write(f'这是新写入的数据（{current_date}）。\n')

# 重新打开文件以读取内容
with open('test_file2.txt', 'r', encoding='utf-8') as f:
    readline_data = f.readline()
    read_data = f.read()
    print('readline_data::', readline_data)
    print('------readline------')
    print('read_data::', read_data)
 


print('**************************')
with open('test_file2.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')


print('2222222222222222222222222222222222222222222')
with open('test_file2.txt','a',encoding='utf-8') as f:
     print(f.write('This is a test\n'))
     """写入其他类型的对象前，需要先将类型转成字符串"""
     value = ('the answer', 42)
     s = str(value)  # 将元组转换为字符串
     print(f.write(s),f.tell())


# json
import json

# 追加模式 ('a') 打开文件，写入数据
with open('test_file2.txt', 'a', encoding='utf-8') as f:
    x = [1, 'simple', 'list']
    json_str = json.dumps(x)  # 将 Python 对象转换为 JSON 字符串
    f.write(f'这是新写入的数据（{current_date}）：{json_str}\n')
    

# 重新打开文件以读取内容
with open('test_file2.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')


# 我们可以检测文件是否已被自动关闭。
f.closed

