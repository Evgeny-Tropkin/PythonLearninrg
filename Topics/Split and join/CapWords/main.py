initial_identifier = input().split('_')

right_class_identifier = ''.join([word.capitalize() for word in initial_identifier])

print(right_class_identifier)