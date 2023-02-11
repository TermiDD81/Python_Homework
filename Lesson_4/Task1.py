n = [2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]
m = [3, 6, 9, 12, 15, 18]
l = []
for i in range(len(n)):
    if n[i] in m:
        l.append(n[i])

k = list(set(l))
k.sort()
print(k)