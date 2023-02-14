def sum(a, b):
    if b == 0:
        return a
    if b != 0:
        return sum(a+1, b-1)


a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
print("Сумма чисел =", sum(a, b))