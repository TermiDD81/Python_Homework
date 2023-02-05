import random
n = int(input("Введите длину массива\n"))
mas = []
for i in range(n):
    mas.append(random.randint(0, 10))
print(mas)
x = int(input(f"Введите число от 0 до {n}\n"))
if x in mas:
    print(f"Ближайшее максимальное число {x}")
else:
    mas.sort()
    for j in range(n):
        if x < mas[j]:
            if mas[j] - x > x - mas[j-1] and x != 0:
                print(f"Ближайшее максимальное число  {mas[j-1]}")
            else:
                print(f"Ближайшее максимальное число  {mas[j]}")
            break
    else:
        print(f"Ближайшее максимальное число {mas[j]}")