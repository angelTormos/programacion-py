num1 = int(input("Introduce el primer numero "))
num2 = int(input("Introduce el segundo numero "))

if num1 % 2 == 0:
    print (num1)
    while num1 < num2:
        num1 = num1 + 2
        print(num1)
else:
    num1 = num1 + 1
    print(num1)
    while num1 < num2:
        num1 = num1 + 2
        print(num1)