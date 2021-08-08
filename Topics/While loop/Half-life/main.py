initial_atoms_quantity = int(input())
final_atoms_quantity = int(input())

HALF_LIFE_PERIOD_LENGTH_IN_DAYS = 12

current_atoms_quantity = initial_atoms_quantity
number_of_half_life_periods = 0
while current_atoms_quantity > final_atoms_quantity:
    current_atoms_quantity //= 2
    number_of_half_life_periods += 1

number_of_days = \
    number_of_half_life_periods * HALF_LIFE_PERIOD_LENGTH_IN_DAYS

print(number_of_days)
