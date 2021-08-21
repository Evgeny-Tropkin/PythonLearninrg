from nltk.tokenize import regexp_tokenize

pattern = "[A-z'-]+"
string = input()

res = regexp_tokenize(string, pattern)
print(res)
