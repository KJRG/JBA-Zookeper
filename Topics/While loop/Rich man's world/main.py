sum_of_deposit = int(input())
number_of_years = 0
while sum_of_deposit < 700000:
    sum_of_deposit *= 1.071
    number_of_years += 1
print(number_of_years)
