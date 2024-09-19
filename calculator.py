## The implementation of a simple calculator

## main()
## add()
## subtract()
## multiply()
def multiply(x, y):
    return x * y
## divide()
def divide (x, y):
  if y == 0:
    print("На ноль делить нельзя")
  else: return(x / y)
## parse()

def subtract():
  num1 = float(input("Введите первое число: "))
  num2 = float(input("Введите второе число: "))
  result = num1 - num2
  print(f"Результат: {result}")
if __name__ == "__main__":
  subtract()
