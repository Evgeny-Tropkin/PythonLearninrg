def get_percentage(number, precision=None):
    value = number * 100
    if precision is None:
        value = int(value)
    else:
        value = round(value, precision)
    return f"{value}%"
