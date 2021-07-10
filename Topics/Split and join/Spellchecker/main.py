dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

words = input().split()
mistake_not_found = True
for word in words:
    if word in dictionary:
        continue
    else:
        print(word)
        mistake_not_found = False
if mistake_not_found:
    print("OK")
