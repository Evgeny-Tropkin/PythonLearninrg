underscored_identifier_parts = input().split('_')
camel_case_identifier = ''.join([word.capitalize() for word in underscored_identifier_parts])

print(camel_case_identifier)
