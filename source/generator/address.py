import json
import random

# File json lưu thông tin về phường xã của cả nước
with open('source/data/info_provinces.json', encoding='utf-8') as file:
    # Thông tin được lưu dưới dạng nested list data
    data = json.load(file)

def all_provinces():
    province_code = {} # Lưu địa chỉ + mã vùng của địa chỉ
    code_set = set() # Lưu mã vùng của 63 tỉnh thành

    # Loop qua từng nested list trong data
    for province in data:
        # Gán tên tỉnh/tp vào province_name
        province_name = province["name"]
        # Lấy mã vùng của tỉnh đó
        code = province["code"]
        code_set.add(code)
        for district in province["districts"]:
            # Gán tên quận/huyện vào district_name
            district_name = district["name"]
            for ward in district["wards"]:
                # Gán tên phường/xã vào ward_name
                ward_name = ward["name"]
                # Kết hợp lại và thêm vào list province_code
                full_name = ward_name + ", " + district_name + ", " + province_name
                province_code[full_name] = code

    # Trả về set mã vùng và dict địa chỉ - mã vùng
    return code_set, province_code

def get_school_address(size): # Size để lưu số địa chỉ cần phải sinh
    # List để lưu mã vùng của các tp trực thuộc trung ương
    # HN - 1; HCM - 79; HP - 31; ĐN - 48; CT - 92
    city_code = [1, 79, 31, 48, 92]
    address = []
    # Lấy các giá trị trả về từ hàm all_provinces()
    code_set, add_code = all_provinces()

    # Loại bỏ các mã vùng thành phố trong code_set
    for i in city_code:
        code_set.discard(i)

    for city in city_code:
        if city == 1 or city == 79: # Nếu mã vùng là HN hoặc HCM
            matching_keys = [key for key, value in add_code.items() if value == city]
            # Lấy random từ 10-15 địa chỉ
            num_samples = random.randint(10, 15)
        else:
            matching_keys = [key for key, value in add_code.items() if value == city]
            # Các tp còn lại thì lấy 5-10 địa chỉ
            num_samples = random.randint(5, 10)
        # Lấy random các địa chỉ đã được lấy ở trên
        random_samples = random.sample(matching_keys, k=min(num_samples, size))
        # Thêm vào list address
        address.extend(random_samples)
        # Với mỗi n địa chỉ đã sinh, trừ bớt vào size
        size -= len(random_samples)
        if size <= 0:
            break

    # Lặp với size sau khi đã trừ n địa chỉ thành phố trung ương
    for index in range(size):
        # Chọn ngẫu nhiên địa chỉ của các tỉnh
        rand_code = random.choice(list(code_set))
        matching_keys = [key for key, value in add_code.items() if value == rand_code]
        # Đối với các tỉnh thành không trực thuộc trung ương, random ngẫu nhiên từ 1-3 địa chỉ
        num_samples = random.randint(1, 3)
        num_samples = min(num_samples, size)
        random_samples = random.sample(matching_keys, k=num_samples)
        address.extend(random_samples)
        size -= len(random_samples)
        if size <= 0:
            break
        # Sau khi đã lấy địa chỉ của tỉnh A, xóa tỉnh A ra khỏi danh sách
        code_set.discard(rand_code)

    return address


def get_student_address(size):
    # Lấy dict địa chỉ - mã vùng
    _, add_code = all_provinces()
    # Lấy phần địa chỉ và lưu vào dict add_keys
    add_keys = list(add_code.keys())
    # Lấy ngẫu nhiên địa chỉ từ list add_keys
    student_addresses = random.choices(add_keys, k=size)

    return student_addresses
