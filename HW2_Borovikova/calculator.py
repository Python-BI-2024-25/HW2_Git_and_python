#  Addition
def addition(n1, n2):
	return n1 + n2


#Напишите функцию здесь
def main():
  built = (input()).split()
  number1=float(built[0])
  number2=float(built[2])
  if built[1] == '+':
    print(addition(number1,number2))
  elif built[1] == '-':
     print(substraction(number1,number2))
  elif built[1] == '*':
    print(multiplication(number1,number2))
  elif built[1] == '/':
    print(divison(number1,number2)) 
main()
