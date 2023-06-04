import json
import random
with open('source/data/info_provinces.json', encoding='utf-8') as file:
    data = json.load(file)

def all_provinces():
    add_code = {}
    code_set = set()
    for province in data:
        province_name = province["name"]
        code = province["code"]
        code_set.add(code)
        for district in province["districts"]:
            district_name = district["name"]
            for ward in district["wards"]:
                ward_name = ward["name"]
                full_name = ward_name + ", " + district_name + ", " + province_name
                add_code[full_name] = code

    #Trả về set mã vùng và dict địa chỉ - mã vùng
    return code_set, add_code

def get_school_address(size):
    city_code = [1, 79, 31, 48, 92]
    address = []
    code_set, add_code = all_provinces()

    for i in city_code:
        code_set.discard(i)

    for city in city_code:
        # Random address for HN and HCM (10 - 15 schools)
        if city == 1 or city == 79:
            matching_keys = [key for key, value in add_code.items() if value == city]
            num_samples = random.randint(10, 15)
        # Random address for Hai Phong, Da Nang va Can Tho (5- 10 schools)
        else:
            matching_keys = [key for key, value in add_code.items() if value == city]
            num_samples = random.randint(5, 10)
        random_samples = random.sample(matching_keys, k=min(num_samples, size))
        address.extend(random_samples)
        size -= len(random_samples)
        if size <= 0:
            break

    for index in range(size):
        rand_code = random.choice(list(code_set))
        matching_keys = [key for key, value in add_code.items() if value == rand_code]
        num_samples = random.randint(1, 3)
        num_samples = min(num_samples, size)
        random_samples = random.sample(matching_keys, k=num_samples)
        address.extend(random_samples)
        size -= len(random_samples)
        if size <= 0:
            break
        code_set.discard(rand_code)

    return address


def get_student_address(size):
    _, add_code = all_provinces()
    add_keys = list(add_code.keys())
    student_addresses = random.choices(add_keys, k=size)

    return student_addresses
