import random
n = int(input("Введите длину массива\n"))
mas = []
for i in range(n):
    mas.append(random.randint(0, 10))
print(mas)
x = int(input("Введите число\n"))
print(f"число {x} встречается {mas.count(x)} раз")