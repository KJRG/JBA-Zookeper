# put your code here
number = 0
counter = 0
sum_of_inputs = 0
average = 0
while number != 55:
    number = int(input())
    if number != 55:
        counter += 1
        sum_of_inputs += number
if counter != 0:
    average = round(sum_of_inputs / counter)
print(counter)
print(sum_of_inputs)
print(average)
