def divide(a, b):
    """Функция для деления"""
    if b == 0:
        return "Ошибка: Деление на ноль!"
    return a / b

def p_multiply (a, b):
    """Функция умножения"""
    return(a * b)

def sum_lesha(a, b):
    """Функция сложения"""
    return(a + b)

def main():
    """Главная функция для обработки ввода"""
    expression = input("Введите выражение (например, 5 + 3): ")
    parts = expression.split()
    
    if len(parts) != 3:
        print("Ошибка: неверный формат выражения!")
        return
    
    try:
        a = float(parts[0])
        operator = parts[1]
        b = float(parts[2])
    except ValueError:
        print("Ошибка: Неверный ввод чисел!")
        return

    if operator == '+':
        result = sum_lesha(a, b)
    elif operator == '-':
        result = subtract(a, b)
    elif operator == '*':
        result = p_multiply(a, b)
    elif operator == '/':
        result = divide(a, b)
    else:
        print("Ошибка: Неверный оператор!")
        return

    print(f"Результат: {result}")

main()
