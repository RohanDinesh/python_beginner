
def exponent_fun(base_num,power):
    result=1
    for i in range(0,power):
        result*=base_num

    print(result)

base_num,power=input("enter a base number and its power\n").split()

print(base_num +"^"+ power + " is")
exponent_fun(int(base_num),int(power))