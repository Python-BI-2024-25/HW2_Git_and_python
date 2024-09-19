## Implementation of a simple calculator

## main()
def main():
    expression = input()
    expression = expression.split(" ")
    
    x = float(expression[0])
    operator = expression[1]
    y = float(expression[2])

    if operator == '+':
        result = add(x, y)
    elif operator == '-':
        result = subtract(x, y)
    elif operator == '*':
        result = multiply(x, y)
    elif operator == '/':
        result = divide(x, y)
    else:
        result = "Не то!"

    print(result)

## add()
def add(x, y):
    return x + y
    
## subtract()
def subtract(x, y):
  return x - y
    
## multiply()
def multiply(x, y):
    return x * y
    
## divide()
def divide (x, y):
  if y == 0:
    return На ноль делить нельзя"
  else: return(x / y)
      

if __name__ == "__main__":
    main()
  
