def calculate_total_numbers() -> list:
    with open('input.txt', 'r') as file:
        data_list = [lines.strip() for lines in file]

    return data_list


def find_numbers_in_list():
    list_for_analysis = calculate_total_numbers()
    digits_list_by_line = []
    total_sum_of_digits = 0

    for line in list_for_analysis:
        digits = [char for char in line if char.isdigit()]
        digits_list_by_line.append(digits)

    for digits_list in digits_list_by_line:
        if len(digits_list) == 1:
            digit = digits_list[0]
            number = int(digit + digit)
            total_sum_of_digits = total_sum_of_digits + number

        else:
            first_digit = digits_list[0]
            last_digit = digits_list[-1]
            number = int(first_digit + last_digit)
            total_sum_of_digits = total_sum_of_digits + number

    print(total_sum_of_digits)


find_numbers_in_list()
