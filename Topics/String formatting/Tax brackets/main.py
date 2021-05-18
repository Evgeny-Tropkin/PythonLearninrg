income_in_dollars = int(input())
tax_percentage = 0
calculated_tax = 0

if income_in_dollars >= 132407:
    tax_percentage = 28
elif income_in_dollars >= 42708:
    tax_percentage = 25
elif income_in_dollars >= 15528:
    tax_percentage = 15

calculated_tax = round(income_in_dollars * tax_percentage / 100)

print(f"The tax for {income_in_dollars} is {tax_percentage}%. That is {calculated_tax} dollars!")
