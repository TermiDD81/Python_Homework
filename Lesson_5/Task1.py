def power(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    if b != 1:
        return a * power(a, b-1)


a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
print("Результат возведения в степень =", power(a, b))
