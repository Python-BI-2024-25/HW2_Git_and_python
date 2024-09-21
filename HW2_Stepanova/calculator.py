# функция, которая спрашивает, хочет ли человек продолжить расчет
def end():
    while True:
        x = input('Вы хотите совершить еще один расчет?\nОтвет: да/нет ').lower()
        if x == 'да':
            return False
            break
        elif x == 'нет':
            return True
            break
        else: 
            print('Неподходящий ответ')

# функция возвращает F или T, соотвественно, в цикле ее можно указать в виде if end():
# if end():
#     print('Конец программы')
# else:
#     print('Расчет дальше')

def  get_numbers():
    exp = (input("Введите выражение: "))
    return exp

def operation(expression):
    a,oper,b=expression.split()
    a=float(a)
    b=float(b)
    return(a,b,oper)


def calculate(a, b, oper):
    if oper == "+":
        result = a + b
    elif oper == "-":
        result = a - b
    elif oper == "*":
        result = a * b
    elif oper == "/":
        if b != 0:
            return a / b
        else:
            return "Ошибка: Деление на ноль!"
    else:
        result = "Я умею только складывать, вычитать, умножать и делить"
    return result

def display(result):
    print("Результат: ", result)

def main():
     while True:
    # Получение чисел
        exp = get_numbers()

    # Запрос операции
        a,b,oper = operation(exp)

    # Вычисление
        result = calculate(a, b, oper)

    # Вывод результат
        display(result)

    #Реализует функцию end()
        if end():
            print('Конец программы')
            break

if __name__ == "__main__":
    main()
