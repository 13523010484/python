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



