num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))

if num1 == num2:
    print("Числа рівні")
elif num1 > num2:
    print(num2, num1)
else:
    print(num1, num2)