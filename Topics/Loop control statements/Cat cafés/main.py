max_cats_num = 0
cafe_name = ""

while True:
    cafe_information = input()
    if cafe_information == "MEOW":
        break
    num = int(cafe_information.split(" ")[1])
    if num > max_cats_num:
        max_cats_num = num
        cafe_name = cafe_information.split(" ")[0]

print(cafe_name)
