def is_duplicate(needle, haystack):
    exist_counter = 0
    for straw in haystack:
        if straw.lower() == needle.lower():
            exist_counter += 1

    return exist_counter > 1


def read_data(filepath):
    with open(filepath, "r") as f:
        return f.read().splitlines()


def find_duplicates(source):
    duplicates = []

    for entry in source:
        if is_duplicate(entry, source):
            duplicates.append(entry)

    return set(duplicates)


if __name__ == "__main__":
    source = read_data("fixtures/names.txt")
    print(find_duplicates(source))
