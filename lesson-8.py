# SyntaxError: invalid syntax 语法错误（解析错误）
# while True print('Hello world')

while True:
    try:
        x = int(input("please enter a number: "))
        break
    except ValueError:
        print("")