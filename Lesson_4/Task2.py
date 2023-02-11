import random
m = int(input("Введите количество кустов\n"))
n = []
max = 0
for i in range(m):
    n.append(random.randint(0, 10))
print(n)
for i in range(1, len(n) - 1):
    if n[i] + n[i-1] + n[i+1] > max:
        max = n[i] + n[i-1] + n[i+1]
if n[-2] + n[-1] + n[0] > max:
    max = n[-2] + n[-1] + n[0]
if n[-1] + n[0] + n[1] > max:
    max = n[-1] + n[0] + n[1]
print(max)
