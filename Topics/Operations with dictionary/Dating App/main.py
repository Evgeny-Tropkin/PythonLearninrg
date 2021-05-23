def select_dates(potential_dates):
    desired_age = 30
    desired_hobby = "art"
    desired_city = "Berlin"
    result = [person["name"] for person in potential_dates if (person["age"] > desired_age
                                                               and desired_hobby in person["hobbies"]
                                                               and person["city"] == desired_city)]
    return ", ".join(result)
