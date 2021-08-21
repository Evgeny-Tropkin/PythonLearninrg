from nltk.tokenize import regexp_tokenize
from nltk.tokenize import sent_tokenize


text = input()
number_of_sentence = int(input())
pattern = "[A-z']+"

sentences = sent_tokenize(text)
res = regexp_tokenize(sentences[number_of_sentence], pattern)
print(res)
