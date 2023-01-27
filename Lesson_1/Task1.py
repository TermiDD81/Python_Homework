a = int(input("Введите 3-х значное число\n"))
a3 = a % 10
a2 = (a // 10) % 10
a1 = a // 100
print(a1, a2, a3)
print(a1 + a2 + a3)
