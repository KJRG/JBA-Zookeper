number_of_halls = int(input())
single_hall_capacity = int(input())
number_of_viewers = int(input())
enough_places =\
    number_of_viewers <= (number_of_halls * single_hall_capacity)
print(enough_places)
