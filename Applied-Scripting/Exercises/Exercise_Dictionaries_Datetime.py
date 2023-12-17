import datetime


def get_next_birthday(dob):
    
    date_string = dob.split("/")

    today = datetime.datetime.now()

    birth_day = datetime.datetime( today.year, int(date_string[1]), int(date_string[0]))

    if birth_day > today:
        return birth_day.strftime("%d/%m/%Y")
    else:
        next_birth_day = birth_day + datetime.timedelta(days = 366)
        return next_birth_day.strftime("%d/%m/%Y")


# Michael D Higgins, President of Ireland
birthday_string = get_next_birthday("18/4/1941")
print(f"Next birthday: {birthday_string}")