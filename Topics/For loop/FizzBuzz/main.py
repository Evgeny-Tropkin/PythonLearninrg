for num in range(1, 101):
    str_for_printing = ""
    num_mod_3 = num % 3
    num_mod_5 = num % 5
    if num_mod_3 != 0 and num_mod_5 != 0:
        print(num)
        continue

    if num_mod_3 == 0:
        str_for_printing += "Fizz"
    if num_mod_5 == 0:
        str_for_printing += "Buzz"

    print(str_for_printing)
