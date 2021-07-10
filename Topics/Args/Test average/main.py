def average_mark(*marks):
    s = 0
    for mark in marks:
        s += mark
    return round(s / len(marks), 1)
