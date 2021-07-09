sentence = input().split()

print('_'.join([word for word in sentence if word[-1] == 's']))
