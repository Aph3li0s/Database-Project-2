import random
from datetime import date
from datetime import timedelta

# Hàm random ngày tháng năm sinh
def rand_year(size):
    # Dữ liệu học sinh cấp 3 nên set năm từ 2k5 - 2k7
    start_year = 2005
    end_year = 2007
    rand_birthday = []
    # Range từ 1/1/2005 đến 31/12/2007
    start_date = date(start_year, 1, 1)
    end_date = date(end_year, 12, 31)

    # Tạo và lưu giá trị đến khi độ dài của list = size
    while len(rand_birthday) != size:
        time_difference = (end_date - start_date).days
        random_days = random.randint(0, time_difference)
        random_date = start_date + timedelta(days=random_days)
        rand_birthday.append(random_date.strftime("%Y/%m/%d"))

    return rand_birthday
