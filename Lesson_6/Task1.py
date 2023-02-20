list_1 = []
for i in range(3):
    n = int(input())
    list_1.append(n)
print(list_1)

list_2 = [list_1[0]]
aN = list_1[0]
for j in range(list_1[2] - 1):
    list_2.append(aN + (j + 1) * list_1[1])
print(list_2)