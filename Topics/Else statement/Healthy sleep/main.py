min_recommended_time = int(input())
max_recommended_time = int(input())
time_for_sleep = int(input())

if time_for_sleep < min_recommended_time:
    print("Deficiency")
elif time_for_sleep > max_recommended_time:
    print("Excess")
else:
    print("Normal")
