ticketNumber = int(input("Введите номер билета (6-ти значное число)\n"))
firstNumbers = ticketNumber // 1000
sumFN = firstNumbers // 100 + (firstNumbers // 10) % 10 + firstNumbers % 10
lastNumbers = ticketNumber % 1000
sumLN = lastNumbers // 100 + (lastNumbers // 10) % 10 + lastNumbers % 10
if sumFN == sumLN:
    print("Ура, билет счастливый!")
else:
    print("Ничего, день и так хороший!")