start_num = int(input())
end_num = int(input())

divided_by_3 = list(filter(lambda num: num % 3 == 0, range(start_num, end_num + 1)))
print(sum(divided_by_3)/len(divided_by_3))
