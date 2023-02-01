import math
sum = int(input("Введите сумму чисел\n"))
multiplication = int(input("Введите произведение чисел\n"))
number1 = (sum - math.sqrt(sum ** 2 - 4 * multiplication)) / 2
number2 = sum - number1
print("Первое число = ", int(number1))
print("Второе число = ", int(number2))