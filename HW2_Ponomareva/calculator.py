#! /usr/bin/env python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Делить на ноль нельзя!"

def main():
   #  
    list_action = input('Введите выражение: ').split()

    # 
    if list_action[1] in ['*', '/', '+', '-']:
        operator = list_action[1]
        num1 = float(list_action[0])
        num2 = float(list_action[2])
        if operator == '+':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif operator == '-':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif operator == '*':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif operator == '/':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Я так не умею!")            
                

main()
