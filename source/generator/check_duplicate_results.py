from collections import Counter


def check_distinct(a):
    counter = Counter(a)
    duplicates = [element for element, count in counter.items() if count > 1]

    if duplicates:
        print("Duplicate elements found:")
        print(duplicates)
    else:
        print("No duplicate elements found.")

    print("Total students: " + str(len(a)))
