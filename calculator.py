# Description - program calculates basic mathematical operations: +,-,*,/
# Input - user enters numbers and operation sign
# Output - calculated number
# Authors: Калинина, Козлова, Субракова, Финк


def add(x, y):
       return x + y
def multiply(x,y):
       return x * y
def divide(x, y):
    if y == 0:
        return "Ошибка! Деление на ноль."
    else: 
        return x / y  
def minus(x, y):
       return x - y 

def main():
    inp = input("Введите выражение, используя пробелы до и после оператора, дробные числа должны быть разделены .")

    string_to_list = inp.split( )
    a = float(string_to_list[0])
    b = float(string_to_list[2])
    operator = string_to_list[1]

    if operator == '+':
        result = add(a, b)
    elif operator == '*':
        result = multiply(a, b)
    elif operator == '/':
        result = divide(a, b)
    elif operator == '-':
        result = minus(a, b)
    return result
print(main())
