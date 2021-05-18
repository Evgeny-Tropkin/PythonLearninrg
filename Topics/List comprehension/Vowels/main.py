vowels = 'aeiou'
string = input()

new_list = [char for char in string if char in vowels]
print(new_list)
