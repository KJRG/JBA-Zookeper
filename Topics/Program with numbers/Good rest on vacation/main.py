# put your python code here
duration_in_days = int(input())
food_cost_per_day = int(input())
one_way_flight_cost = int(input())
night_in_hotel_cost = int(input())

total_cost =\
    (duration_in_days * food_cost_per_day)\
    + (2 * one_way_flight_cost)\
    + ((duration_in_days - 1) * night_in_hotel_cost)

print(total_cost)
