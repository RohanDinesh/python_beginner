num1 = input(" enter first number: ")
op = input("enter an operator: ")
num2 = input(" enter second number: ")

if(op=='+'):
    sum = int(num1) + int(num2)
    print(sum)

elif(op=='-'):
    diff = int(num1) - int(num2)
    print(diff)

elif(op=='*'):
    mul = int(num1) * int(num2)
    print(mul)

elif(op=='/'):
    div = int(num1) / int(num2)
    print(div)

else:
    print("invalid operator")





