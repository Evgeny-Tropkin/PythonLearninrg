duration_in_days = int(input())
total_food_cost_per_day = int(input())
one_way_flight_coast = int(input())
cost_of_the_night = int(input())

price_of_vacation = (duration_in_days - 1) * cost_of_the_night + one_way_flight_coast * 2 \
                    + total_food_cost_per_day * duration_in_days
print(price_of_vacation)
