def subst(num1, num2):
    #Вычитание
    return num1 - num2 


def mult(num1, num2):
    #Умножение
    return num1 * num2


def div(num1, num2):
    #Деление
    return num1 / num2


def plus(num1, num2):
    #Сложение
    return num1 + num2


def main():
    expression = input('Введите математическое выражение, используя 2 переменные и символы "+", "-", "*", "/": ')
    some_parts = expression.split()
    num1, operator, num2 = some_parts
    num1 = float(num1)
    num2 = float(num2)
    if (operator == '*'):
        result = mult(num1, num2)
    elif (operator == '/'):
        result = div(num1, num2)
    elif (operator == '-'):
        result = subst(num1, num2)
    elif (operator == '+'):
        result = plus(num1, num2)
    print(result)


if __name__ == "__main__":
    main()
