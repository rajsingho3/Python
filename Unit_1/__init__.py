# Swapping two number
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("Before swapping :", num1, num2)
# Swapping two number without using third variable
num1 = num1+ num2
num2 = num1 - num2
num1 = num1 - num2
print("After swapping :", num1 , num2)