prime_numbers = [2]
limit = 1000

if limit > 2:
    numbers = [False, False, True] + [True, False] * ((limit - 2) // 2)
    current_divider = 3
    while (current_divider * current_divider) < limit:
        for pos in range(current_divider * current_divider, limit + 1, current_divider * 2):
            numbers[pos] = False
        prime_numbers.append(current_divider)
        try:
            current_divider = numbers.index(True, current_divider + 1)
        except ValueError:
            break
    else:
        prime_numbers.append(current_divider)
        for _ in range(current_divider, limit + 1):
            try:
                current_divider = numbers.index(True, current_divider + 1)
                prime_numbers.append(current_divider)
            except ValueError:
                break
