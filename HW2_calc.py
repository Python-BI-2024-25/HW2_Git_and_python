str = input()
counter = 0
result = 0
for i in str:
    if i == "+" or i == "-" or i == "/" or i == "*":
        op = i
        counter += 1
        break
    else:
        counter += 1
        continue
f_num = int(str[0:counter-1])
s_num = int(str[counter+1:len(str)+1])
if op == "*":
    result = f_num * s_num
print(result)