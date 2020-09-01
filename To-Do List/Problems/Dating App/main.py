def select_dates(potential_dates):
    result = ''
    for person in potential_dates:
        if person["city"] == "Berlin" and person["age"] > 30 and "art" in person["hobbies"]:
            result += person["name"] + ', '
    return result[0:len(result) - 2]
