import random
from datetime import date
from datetime import timedelta


def rand_year(size):
    start_year = 2005
    end_year = 2007
    rand_birthday = []
    start_date = date(start_year, 1, 1)
    end_date = date(end_year, 12, 31)

    while len(rand_birthday) != size:
        time_difference = (end_date - start_date).days
        random_days = random.randint(0, time_difference)
        random_date = start_date + timedelta(days=random_days)
        rand_birthday.append(random_date.strftime("%Y/%m/%d"))

    return rand_birthday
