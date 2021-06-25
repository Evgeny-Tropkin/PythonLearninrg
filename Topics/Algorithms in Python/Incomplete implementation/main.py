def startswith_capital_counter(names):
    if not names:
        return -1
    count = 0
    for name in names:
        f = name[0]
        if 'A' <= f <= 'Z':
            count += 1
    return count
