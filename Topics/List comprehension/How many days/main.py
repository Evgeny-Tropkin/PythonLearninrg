seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]

full_days = [seconds_count // 86400 for seconds_count in seconds]
print(full_days)
