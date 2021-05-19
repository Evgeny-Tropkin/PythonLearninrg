sample_file = open("sample.txt", "r")
strings = sample_file.readlines()
print(len(strings))
sample_file.close()
