def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0 :
        return "Error! zero can't devide"
    return a / b

print("----SIMPLE CALCULATER----")



while True:

    num1 = int(input("Enter your number : "))
    num2 = int(input("Enter your number : "))

    print("1. Add + ")
    print("2. Subtract - ")
    print("3. Multiply X ")
    print("4. Divide / ")

    chice = int(input("Enter Chice ( 1 / 2 / 3 / 4) : "))



    if chice == 1 :
        print(add(num1,num2))
    
    elif chice == 2 :
        print(subtract(num1,num2))

    elif chice == 3 :
        print(multiply(num1, num2))

    elif chice == 4 :
        print(divide(num1,num2))
    else:
        print("Invalede Number ! .....")


