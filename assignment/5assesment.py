num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("both greater than 10:",num1>10 and num2<10)
print("at least one less than 5:",num1<5 or num2<5)
print("first number not grater then second:",not(num1>num2))