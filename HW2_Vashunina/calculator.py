def fun_minus(num_1,num_2):
   return float(num_1) - float(num_2)

def fun_div(num_1,num_2):
   return float(num_1) / float(num_2)

def fun_sum(num_1,num_2):
   return float(num_1) + float(num_2)

def fun_mult(num_1,num_2):
   return float(num_1) * float(num_2)

def main():
    line = str(input()).split()
    num_1 = line[0]
    num_2 = line[2]
    operator = line[1]
    if operator == "-":
      return fun_minus(num_1,num_2)
    if operator == "/":
      return fun_div(num_1,num_2)
    if operator == "+":
      return fun_sum(num_1,num_2)
    if operator == "*":
      return fun_mult(num_1,num_2)
