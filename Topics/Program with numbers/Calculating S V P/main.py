# put your python code here
length = int(input())
width = int(input())
height = int(input())

sum_of_edges_length = 4 * (length + width + height)
surface_area =\
    2 * (
        (length * width)
        + (width * height)
        + (length * height)
    )
volume = length * width * height

print(sum_of_edges_length)
print(surface_area)
print(volume)
