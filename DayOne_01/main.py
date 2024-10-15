def calculate_total_numbers() -> list:
    with open('input.txt', 'r') as file:
        lines_list = [lines.strip() for lines in file]

    print(lines_list)
    return lines_list


calculate_total_numbers()
