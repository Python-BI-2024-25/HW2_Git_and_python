# функция для расчёта суммы двух чисел
def add(a, b):
    return a + b
# функция для расчёта разницы двух чисел
def subtract(a, b):
    return a - b
#  функция ввода/ вывода
def main():
    # Получаем дашнные от юзера
    expression = input("Введите выражение (пример: 5 - 3): ")

    # Разбиваем строку на части
    arguments = expression.split()

    #Проверяем, что выражение верное
    if len(arguments) != 3:
        print("Ошибка ввода! Пробелы перед и после знака оператора, потом жмём Enter")
        return

    num1_str, operator, num2_str = arguments

    try:
        # Преобразуем в float для корректной работы с вещественными числами
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        print("Ошибка в формате числа!")
        return

    # Выбор операции
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    else:
        print("Ошибка! Выбрать + - / *")
        return

    print(f"Результат: {result}")

main()
