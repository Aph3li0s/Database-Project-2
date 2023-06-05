import random

def rand_cccd(size):
    # Dùng set để lưu giá trị duy nhất
    cccd = set()

    # Nếu độ dài của chuỗi chưa đủ 12
    while len(cccd) != size:
        # Random chữ số ngẫu nhiên và thêm vào chuỗi
        num = ''.join(str(random.randint(0, 9)) for _ in range(12))
        cccd.add(num)
    return cccd
