
def plus_hw(arg1, arg2):
    return arg1 + arg2


def minus_hw(arg1, arg2):
    return arg1 - arg2


def multi_hw(a, b):
    return a * b


def div_hw(arg1, arg2):
    if arg2 == 0.0:
        return 'Error: division by zero'
    return arg1 / arg2


def main():
    arg1, operation, arg2 = input().split()
    if "." in arg1:
        arg1 = float(arg1)
    else:
        arg1 = int(arg1)
    if "." in arg2:
        arg2 = float(arg2)
    else:
        arg2 = int(arg2)
    #arg1, arg2 = map(int, [arg1, arg2])
    if operation == '+':
        answ = plus_hw(arg1, arg2)
    elif operation == '-':
        answ = minus_hw(arg1, arg2)
    elif operation == '*':
        answ = multi_hw(arg1, arg2)
    elif operation == '/':
        answ = div_hw(arg1, arg2)
    print(answ)

while True:
    main()


