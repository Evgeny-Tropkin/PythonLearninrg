# read test_file.txt
test_file = open("test_file.txt", "r", encoding="UTF-16")
print(test_file.readline())
test_file.close()
