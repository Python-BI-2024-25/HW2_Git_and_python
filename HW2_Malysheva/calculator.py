def main(string):
    for_calculating = string.split()
    if "+" in for_calculating:
        return summation(for_calculating)
    elif "-" in for_calculating:
        return substraction(for_calculating)
    elif "*" in for_calculating:
        return multiplication(for_calculating)
    elif "/" in for_calculating:
        return dividing(for_calculating)
    else:
        print("Что-то не так с введенными данными, проверь!")

def dividing(for_calculating):
    operand1 = float(for_calculating[0])
    operand2 = float(for_calculating[2])
    if operand2 == 0:
        return "Ошибка: Деление на ноль"
    result = operand1 / operand2
    return result

def summation(for_calculating):
    ans=float(for_calculating[0])+float(for_calculating[2])
    return ans
  
def is_float(n: str) -> bool:
     try:
         float(n)
         return True
     except ValueError:
         return False
      
def multiplication(for_calculating):
  if is_float(for_calculating[0]) and is_float(for_calculating[2]):
    return float(for_calculating[0]) * float(for_calculating[2])
  else:
    print('Что-то не так с введенными данными, проверь!')

def subtraction(for_calculating):
  numbers = []
  for i in for_calculating:
    if i.isnumeric() or is_float(i):
        numbers.append(float(i))
  return(numbers[0] - numbers[1])

string = input("Введите математическую операцию: ")
print(main(string))
