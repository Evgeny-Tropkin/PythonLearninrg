day_of_week = "Tuesday"
reference_time = 10.5
offset = int(input())

calculated_time = reference_time + offset

if calculated_time < 0:
    day_of_week = "Monday"
elif calculated_time > 24:
    day_of_week = "Wednesday"

print(day_of_week)
