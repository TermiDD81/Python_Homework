nCoin = int(input("Введите количество монеток\n"))
i = attempt = eagle = tails = 0
while i < nCoin:
    attempt = int(input("Орел  или решка? (0 или 1)\n"))
    i += 1
    if attempt == 0:
        eagle += 1
    else:
        tails += 1
if eagle > tails:
    print("минимальное количество монет, которые нужно перевернуть = ", nCoin - eagle)
else:
    print("минимальное количество монет, которые нужно перевернуть = ", nCoin - tails)