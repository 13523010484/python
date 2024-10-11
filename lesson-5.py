fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# count 数组中项的个数
print(fruits.count('apple'))
print(fruits.count('banana'))
# index 数组中项的索引
print(fruits.index('apple'))
# 从索引 4 开始查找下一个 banana
print(fruits.index('banana',4))
# reverse 倒序排
fruits.reverse()
print(fruits)

fruits.sort(reverse=False)
print('reverse=False::',fruits)

fruits.sort(reverse=True)
print('reverse=True::',fruits)

fruits.pop()
print('pop::',fruits)

# 栈
stack = ['web','java','sql']
stack.append('test')
print('stack.appent::',stack)

stack.pop()
print('stack.pop::',stack)


# 列表实现队列
from collections import deque
queue = deque(['a','b','c'])
print('queue::',queue)

queue.append('d')
print('queue.append::',queue)

queue.popleft()
# 删除队列头部
print('queue.popleft::',queue)


# 列表推到式
squares = []
for x in range(10):
    squares.append(x**2)
print('squares::',squares,x)

# 无副作用计算平方
squares2 = list(map(lambda x: x**2,range(10)))
print('squares2::',squares2,x)

# 以上等价于
squares3 = [x**2 for x in range(10)]
print('squares3::',squares3,x)

# 双层循环推导式
forDemo = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print('forDemo::',forDemo)

# 上面的等价于
forDemo2 = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            forDemo2.append((x, y))
print('forDemo2::',forDemo2)


# 创建翻倍的列表
vec = [-1,-2,0,1,2,3,4,5,6]
vecDouble = [x*2 for x in vec]
print('vec::',vec,'vecDouble::',vecDouble)

# 找出数组中的偶数
vecEven = [x for x in vec if x % 2 == 0]
print('vec::',vec,'vecEven::',vecEven)

# 找出数组中的奇数
vecOdd = [x for x in vec if x % 2 == 1]
print('vec::',vec,'vecOdd::',vecOdd)

# 将数组中的数转换为绝对值
vecAbs = [abs(x) for x in vec]
print('vec::',vec,'vecAbs::',vecAbs)


# 将数组中的字符串去除空格
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
freshfruit2 = [x.strip() for x in freshfruit]
print('freshfruit::',freshfruit,'freshfruit2::',freshfruit2)


# 创建一个数字及数字平方的列表
numList = [(x,x**2) for x in range(1,10)]
print('numList::',numList)

# 使用两个 for 展平嵌套的列表
vec3 = [[1,2,3], [4,5,6], [7,8,9]]
vec4 = [j for x in vec3 for j in x]
print('vec3::',vec3,'vec4::',vec4)



# 列表推导式可以使用复杂的表达式和嵌套函数
from math import pi
mathStr = [str(round(pi, i)) for i in range(1, 6)]
print('mathStr::',mathStr)

# 使用推导式实现矩阵行转列 
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
rowToCol = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print('matrix::',matrix,'rowToCol::',rowToCol)


# del 删除列表中的数据
arrList = [1,2,3,4,5]
del arrList[1:3]
print('arrList::',arrList)
del arrList[:]
print('arrList::',arrList)
arrList.extend([1,2,3,4])
print('arrList::',arrList)
# del arrList # 会抛出异常
arrList.clear()
print('arrList::',arrList)


# 元组和排序
empty = ()
singleton = 'hello',    # <-- 注意末尾的逗号  加上逗号是属于一个元组  不加逗号使用len计算的是字符串的长度
singleton1 = 'hello'
print('empty::',len(empty))
print('singleton::',len(singleton),'singleton1::',len(singleton1))

t = 12345, 54321, 'hello!' 
x, y, z = t
print('x::',x,'y::',y,'z::',z)


# 集合，不会存在重复的
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print('basket::',basket,'orange' in basket) # True

a = set('abcde')
b = set('abf')
print('a 中独有的::',a,
      '存在于a但不存在于b中的字母',a-b,
      'a b 并集',a|b,
      'a b 交集',a&b,
      'a b 的非交集',a ^ b)


a1 = {x for x in 'abracadabra' if x not in 'abc'}
print('a1::',a1)


# 字典
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print('tel::',tel)

tel['jack']
print('tel::',tel)

del tel['sape']
tel['irv'] = 4127
print('tel::',tel)

telList = list(tel)
print('telList::',telList)
sorted(telList)
print('telList::',telList)

# dict 构造字典
dictDemo = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print('dictDemo::',dictDemo)

# 字典推导式
dictSimple = {x: x**2 for x in (2, 4, 6)}
print('dictSimple::',dictSimple)

dictSimple1 = dict(sape=4139, guido=4127, jack=4098)
print('dictSimple1::',dictSimple1)

# 字典的循环 items
dictFor = {'gallahad': 'the pure', 'robin': 'the brave'}
for key,value in dictFor.items():
    print('dict items key::',key,'value::',value)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# 倒序
for i in reversed(range(1, 10, 3)):
    print('i::',i)

print('--------------')
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

print('--------------')
basket1 = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket1)):
    print(f)

print('--------------')
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
print('raw_data::',raw_data)
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)


# 条件控制 while if
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
print(string1 or string2 or string3)


# 序列和其他类型的比较
print((1, 2, 3)              < (1, 2, 4)) # True
print([1, 2, 3]              < [1, 2, 4]) # True
print('ABC' < 'C' < 'Pascal' < 'Python') # True
print((1, 2, 3, 4)           < (1, 2, 4)) # True
print((1, 2)                 < (1, 2, -1)) # True
print((1, 2, 3)             == (1.0, 2.0, 3.0)) # True
print((1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)) # True
