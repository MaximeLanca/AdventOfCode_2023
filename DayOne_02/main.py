import re


def get_alphanumeric_data() -> list:
    with open('input.txt', 'r') as file:
        data_list = [lines.strip() for lines in file]
        print(data_list)
    return data_list


def find_words_in_data_list():
    i = 0
    sub_list = []
    verification_list = []
    total = 0
    data = get_alphanumeric_data()
    word_to_number = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    words_pattern = '|'.join(word_to_number.keys())
    pattern = re.compile(r'(?=(' + words_pattern + r'|\d))')

    for line in data:
        i = i + 1
        matches = pattern.findall(line)
        converted_matches = [word_to_number.get(item, item) for item in matches]
        sub_list.append(converted_matches)

    for item in sub_list:
        if len(item) < 2:
            number = int(item[0] + item[0])
        else:
            number = int(item[0] + item[-1])
        total = total + number
        verification_list.append(number)


find_words_in_data_list()
