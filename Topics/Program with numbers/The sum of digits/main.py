# put your python code here
number = int(input())
hundreds = number // 100
tens = (number - hundreds * 100) // 10
ones = number % 10
sum_of_digits = hundreds + tens + ones
print(sum_of_digits)
