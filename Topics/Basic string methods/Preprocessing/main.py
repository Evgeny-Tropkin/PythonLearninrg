inp = input()
outp = []

for char in inp:
    if char in ['.', ',', '!', '?']:
        continue
    outp.append(char.lower())

print(''.join(outp))
