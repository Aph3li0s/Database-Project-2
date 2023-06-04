def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read().split("\n")
    return data

def gen_name():
    firstname_filename = "source/data/name_data/first.name"
    male_filename = "source/data/name_data/male.name"
    female_filename = "source/data/name_data/female.name"
    common_filename = "source/data/name_data/common_first.name"

    firstnames = read_file(firstname_filename)
    lastnames = read_file(male_filename) + read_file(female_filename)
    common_first = read_file(common_filename)

    merged_first = [str(common_first[i]) + ' ' + str(common_first[j])
                    for i in range(len(common_first)) for j in range(i + 1, len(common_first))] + firstnames
    return lastnames, merged_first

