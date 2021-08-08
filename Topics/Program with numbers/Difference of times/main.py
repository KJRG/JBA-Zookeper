# put your python code here

SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
SECONDS_PER_HOUR = SECONDS_PER_MINUTE * MINUTES_PER_HOUR

walk_beginning_h = int(input())
walk_beginning_m = int(input())
walk_beginning_s = int(input())
rain_beginning_h = int(input())
rain_beginning_m = int(input())
rain_beginning_s = int(input())

hours_difference = rain_beginning_h - walk_beginning_h
minutes_difference = rain_beginning_m - walk_beginning_m
seconds_difference = rain_beginning_s - walk_beginning_s

total_diff_seconds =\
    hours_difference * SECONDS_PER_HOUR\
    + minutes_difference * SECONDS_PER_MINUTE\
    + seconds_difference
print(total_diff_seconds)
