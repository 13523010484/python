def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print('x::',x.r,x.i)



x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print("x.counter::",x.counter)
del x.counter



class Dog:
    kind = 'canine'

    def __init__(self,name):
        self.name = name

d = Dog('Fido')
e = Dog('Buddy')
print('d.kind::',d.kind,'e.kind::',e.kind)


class Dog2:
    tricks = []
    def __init__(self,name):
        self.name = name
    def add_trick(self,trick):
        self.tricks.append(trick)

d2 = Dog2('Fido2')
e2 = Dog2('Buddy2')
d2.add_trick('roll over')
e2.add_trick('play dead')
print(d2.tricks)    


class Dog3:
    def __init__(self,name):
        self.name = name
        self.tricks = []
    
    def add_tricks(self,trick):
        self.tricks.append(trick)

d3 = Dog3('Fido')
e3 = Dog3('Buddy')
d3.add_tricks('roll over')
e3.add_tricks('play dead')
print('d3:',d3.tricks,'e3:',e3.tricks)
        
    

class Warehouse:
    purpose = 'storage'
    region = 'west'

w1 = Warehouse()
print()


def f1(self, x,y):
    return min(x,x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'
    
    h = g

# 创建 C 类的实例
c = C()
print('c.f::',c.f(10, 5))  # 输出: 10
print('c.g::',c.g())  # 输出: 10


class Bag:
    def __init__(self):
        self.data = []
    
    def add(self,x):
        self.data.append(x)

    def addTwice(self,x):
        self.add(x)
        self.add(x)

bag = Bag()
bag.add(1)
print(bag.data)


class Animal:
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def move(self):
        return "Moves"
    
class Cat(Animal):
    def speak(self):
        return "Meow"
    
    def move(self):
        return "Walks"

class Bird(Animal):
    def speak(self):
        return "Chirp"
    
    def move(self):
        return "Flies"
    
cat = Cat("white cat")
print('cat::',cat.name,cat.speak(),cat.move())


# 私有变量
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # 原始 update() 方法的私有副本

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # 为 update() 提供了新的签名
        # 但不会破坏 __init__()
        for key, value in zip(keys, values):
            self.items_list.append((key, value))

# 测试代码
mapping = Mapping([1, 2, 3])
print(mapping.items_list)  # 输出: [1, 2, 3]

subclass = MappingSubclass([('a', 1), ('b', 2)])
print(subclass.items_list)  # 输出: [('a', 1), ('b', 2)]

subclass.update(['c', 'd'], [3, 4])
print(subclass.items_list)  # 输出: [('a', 1), ('b', 2), ('c', 3), ('d', 4)]


from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    dept: str
    salary: int

john = Employee('john','computer lab',1000)
print('john::',john.name,john.dept,john.salary)


class Reverse:
    """对一个序列执行反向循环的迭代器。"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
rev = Reverse('spam')
iter(rev)

for char in rev:
    print('char::',char)


# 生成器
def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield data[index]

for char in reverse('golf'):
    print('char::====',char)


# 生成器表达式
sum = sum(i*i for i in range(10)) # 平方和
print('sum::',sum)



