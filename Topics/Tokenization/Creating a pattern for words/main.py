from nltk.tokenize import regexp_tokenize

sentence = input()
index_of_word = int(input())

pattern = "[A-z]+"

res = regexp_tokenize(sentence, pattern)
print(res[index_of_word])
