import re


def get_data() -> list:
    with open('input.txt', 'r') as file:
        data_list = [lines.strip() for lines in file]
    process_data(data_list)


def process_data(data_list: list):
    rule = {"red": 12, "green": 13, "blue": 14}
    number_list = [i for i in range(0, 101)]

    for data in data_list:
        # print(data)
        position_colon = data.find(":")

        game = data[0:position_colon]
        numeric_pattern = re.compile(r'(\d+)')
        game_numbers = numeric_pattern.findall(game)

        sets = data[position_colon + 1:]
        sets_list = re.split(r'[,;]', sets)
        #print(sets_list)

        for sets in sets_list:
            matches = re.findall(r'[a-zA-Z0-9]+', sets)
            print(matches)


get_data()
