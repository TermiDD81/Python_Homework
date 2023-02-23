alph = "аеёиоуыэюя"
words = input().split()
vowel_letters = [sum([True for j in word if j.lower() in alph]) for word in words]
if all(vowel_letters) and len(set(vowel_letters)) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")