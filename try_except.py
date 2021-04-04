
try :
    value=10/0
    number= int(input("enter a number: "))
    print(number)

except ZeroDivisionError as e:
    print("error occured:")
    print(e)

except ValueError as f:
    print(f)
