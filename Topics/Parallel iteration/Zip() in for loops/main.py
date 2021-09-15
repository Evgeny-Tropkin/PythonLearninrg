# please do not modify the following code
interest_rates = [float(x) for x in input().split(',')]
years = [int(x) for x in input().split(',')]
loan_principles = [int(x) for x in input().split(',')]

# your code here
for item in zip(interest_rates, years, loan_principles):
    print(int(item[0] * item[1] * item[2]))
