def final_deposit_amount(*interest_rates, amount=1000):
    final_amount = amount
    for rate in interest_rates:
        final_amount *= (1 + (rate / 100))

    return round(final_amount, 2)
