import re


def get_alphanumeric_data() -> list:
    with open('input.txt', 'r') as file:
        data_list = [lines.strip() for lines in file]
    return data_list


def find_words_in_data_list():
    total_sum_of_digits = 0
    digits_list_by_line = []
    list_for_analysis = get_alphanumeric_data()
    dict_ref = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    # line = tsgbzmgbonethreedrqzbhxjkvcnm3
    for line in list_for_analysis:
        # decomposed_line = ["tsgbzmgbonethreedrqzbhxjkvcnm","3"]
        decomposed_line = re.findall(r'\d+|[a-zA-Z]+', line)
        for key in dict_ref.keys():
            provisional_list = []
            # data = tsgbzmgbonethreedrqzbhxjkvcnm
            for data in decomposed_line:
                if key in data:
                    provisional_list.append(key)
                    index = decomposed_line.index(data)
                    decomposed_line[index] = provisional_list

        for line in list_for_analysis:
            # Séparer chiffres et lettres
            decomposed_line = re.findall(r'\d+|[a-zA-Z]+', line)            #total_sum_of_digits += dict_ref[key]
                    #print(total_sum_of_digits)
            # Remplacer les parties texte par les clés du dictionnaire
            decomposed_line = [print(decomposed_line)
                key if key in data else data for data in decomposed_line for key in dict_ref]

            print(decomposed_line)
find_words_in_data_list()
#
# for line in list_for_analysis:
#    digits = [char for char in line if char.isdigit()]
#    digits_list_by_line.append(digits)
#
# for digits_list in digits_list_by_line:
#    if len(digits_list) == 1:
#        digit = digits_list[0]
#        number = int(digit + digit)
#        total_sum_of_digits = total_sum_of_digits + number
#
#    else:
#        first_digit = digits_list[0]
#        last_digit = digits_list[-1]
#        number = int(first_digit + last_digit)
#        total_sum_of_digits = total_sum_of_digits + number
#
# print(total_sum_of_digits)
