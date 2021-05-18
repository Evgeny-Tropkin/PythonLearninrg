initial_atom_quantity = int(input())
final_atom_quantity = int(input())
half_life_for_radon_223_in_days = 12
number_of_half_life_periods = 0

current_number_of_atoms = initial_atom_quantity

while current_number_of_atoms > final_atom_quantity:
    current_number_of_atoms /= 2
    number_of_half_life_periods += 1

days = number_of_half_life_periods * half_life_for_radon_223_in_days

print(days)
