def range_sum(numbers, start, end):
    s = 0
    start = int(start)
    end = int(end)
    for num in numbers:
        num = int(num)
        if start <= num <= end:
            s += num
    return s


input_numbers = input(). split()
a, b = input().split()
print(range_sum(input_numbers, a, b))
