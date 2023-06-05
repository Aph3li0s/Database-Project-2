def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read().split("\n")
    return data

# Lấy data họ, tên từ folder name_data
def gen_name():
    # Lấy danh sách họ
    firstname_filename = "source/data/name_data/first.name"
    # Lấy danh sách họ phổ biến (để ghép 2 họ lại với nhau)
    common_filename = "source/data/name_data/common_first.name"
    # Lấy danh sách tên nam và nữ
    male_filename = "source/data/name_data/male.name"
    female_filename = "source/data/name_data/female.name"

    firstnames = read_file(firstname_filename)
    lastnames = read_file(male_filename) + read_file(female_filename)
    common_first = read_file(common_filename)

    # Ghép 2 họ lại với nhau
    merged_first = [str(common_first[i]) + ' ' + str(common_first[j])
                    for i in range(len(common_first)) for j in range(i + 1, len(common_first))] + firstnames
    return lastnames, merged_first

