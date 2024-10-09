print('hello world!')

# 创建一个 range 对象并转换为列表
my_list = list(range(4))

# 打印列表
print(my_list)

sum_list = sum(range(4))

print(sum_list)


# berak 和 continue 语句
arr = list(range(1,10))
print('arr::',arr)
for n in arr:
    print('n::',n,'list::',list(range(2,n)))
    for x in range(2,n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # 循环到底未找到一个因数
        print(n, 'is a prime number')




def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a reapot"
        case _:
            return "Something's wrong with the internet"

print(http_error(4))

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0,y=0):
            print("Origin")
        case Point(x=0,y=y):
            print(f"Y={y}")
        case Point(x=x,y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")   


# 创建一些 Point 对象
p1 = Point(0, 0)       # 原点
p2 = Point(0, 5)       # 在 Y 轴上
p3 = Point(10, 0)      # 在 X 轴上
p4 = Point(3, 4)       # 不在坐标轴上的点
not_a_point = "hello"  # 非 Point 类型的对象

# 调用 where_is 函数
where_is(p1)
where_is(p2)
where_is(p3)
where_is(p4)
where_is(not_a_point)



from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green'\n"))

# 相当于 js 中的 switch case
match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")



# 定义函数
def fib(n):
    """Print a Fibonacci series up to n."""
    a,b=0,1
    while a < n:
        print(a,end="、")
        a,b=b,a+b
    print()

fib(2000)

f = fib
f(100)


def fib2(n):
    """"Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
print('f100::',f100)


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

try:
    result = ask_ok('Do you really want to quit? (y/n): ')
    print('Your choice was:', 'Yes' if result else 'No')
except ValueError as e:
    print(e)



# 默认值 定义 作用域里的函数定义中求值，所以：
i = 5
def f(arg=i):
    print(arg)

i = 6
f()


def f(a,L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


# 不在后序调用之间共享默认值
def f1(a,L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f1(1))
print(f1(2))
print(f1(3))

# 4.9.2 关键字参数
""""kwarg=value 形式的 关键字参数 也可以用于调用函数"""
def parrot(voltage,state='a stiff',action='voom',type='Norwegain Blue'):
    print("-- This parrot wouldn't",action,end=' ')
    print("if you put",voltage,"volts through it.")
    print("-- Lovely plumage, the",type)
    print("-- It's",state,"!")

parrot(1000) # 1 个位置参数
parrot(1000,'two stiff','apple','red')

# 函数传递形参
"""
    kind: 第一个参数是固定的
    *arguments: 这个参数是可变长度的,参数从第二个参数开始算起
    **keywords: 这个参数是字典，传递参数的时候，需要以 key = value 的形式进行传递
"""
def cheeseshop(kind,*arguments,**keywords):
    print("-- Do you have any",kind,"?")
    print("-- I/m sorry, we're all out of",kind)
    for arg in arguments:
        print(arg)
    print("-"*40)
    for kw in keywords:
        print(kw,":",keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

def concat(*args,sep="/"):
    return sep.join(args)

print(concat('how','are','you'))
print(concat('how','are','you',sep=" "))

list1 = list(range(3,6))
print('list1::',list1)
args = [3,6]
list2 = list(range(*args))
print('list2::',list2)


def parrot1(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot1(**d)


# 4.9.6 lambda 表达式
def make_incrementor(n):
    return lambda x: x+n

f = make_incrementor(42)
print(f(1))

pairs = [(1, 'one'), (3, 'three'),(2, 'two'),  (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print('pairs::',pairs)


def my_function():
    """Do nothing, but document it.
    
    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)


def f(ham:str,eggs:str='eggs') -> str:
    print("Annotations:",f.__annotations__)
    print("Auguments:",ham,eggs)
    return ham + 'and' + eggs

f('spam')