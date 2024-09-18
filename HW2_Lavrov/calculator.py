    # Вычитание
def subtraction(a, b):
    return a - b

def main():
    a, operator, b =  input().split()
    
    #Переводим строки в соответствующий тип числовых данных
    a = float(a) if "." in a else int(a)
    b = float(b) if "." in b else int(b)
    
    #Отправляем числа нужной функции на вычисление 
    if operator == "+": print(addition(a, b))
    elif operator == "-": print(subtraction(a, b))
    elif operator == "*": print(multiplication(a, b))
    elif operator == "/" and b != 0: print(division(a,b))
    elif operator == "/" and b == 0: print("Деление на ноль!")

main()
