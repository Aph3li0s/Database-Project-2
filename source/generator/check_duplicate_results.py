from collections import Counter

# Đây là unit test, không năm trong code chính
# Hàm này để check xem trong list truyền vào có các giá trị trùng nhau nào không
def check_distinct(a):
    counter = Counter(a)
    duplicates = [element for element, count in counter.items() if count > 1]
    if duplicates:
        print("Trùng giá trị kìa bạn ơi!")
        print(duplicates)
    else:
        print("List chứa toàn giá trị duy nhất")

