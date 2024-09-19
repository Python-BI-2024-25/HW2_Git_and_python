# Description - program calculates basic mathematical operations: +,-,*,/
# Input - user enters numbers and operation sign
# Output - calculated number
# Authors: Калинина, Козлова, Субракова, Финк


inp = input()

def main(inp):

    string_to_list = inp.split("введите выражение, используя пробелы до и после оператора, дробные числа должны быть разделены .")
    a = float(string_to_list[0])
    b = float(string_to_list[2])
    operator = string_to_list[1]
    return a, b, operator


x, y, operator = main(inp)

def add(x, y):
       return x + y
def multiply(x,y):
       return x*y
def minus(x,y):
       return x-y

if operator == '+':
    result = add(x,y)
elif operator == '*':
    result = multiply(x*y)
elif operator == '-':
    result = minus(x-y)
print(f"Результат: {result}")
    



