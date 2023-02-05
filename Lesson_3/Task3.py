en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}
word = input().upper()
print(sum([k for i in word for k, v in en.items() if i in v]))
