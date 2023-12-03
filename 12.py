from typing import List

numbers = [
    'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
]

def solve(data: List[str]) -> str:
    result = 0

    for line in data:
        first_number = None
        second_number = None
        first_number_pos = None
        second_number_pos = None

        for i, char in enumerate(line):
            if char.isdigit():
                if first_number is None:
                    first_number = char
                    first_number_pos = i

                    if second_number is None:
                        second_number = char
                        second_number_pos = i
                else:
                    second_number = char
                    second_number_pos = i

        for number in numbers:
            number_position = line.find(number)

            if number_position == -1:
                continue

            if first_number_pos is None or first_number_pos > number_position:
                first_number = str(numbers.index(number) + 1)
                first_number_pos = number_position

            number_position = line.rfind(number)

            if second_number_pos is None or second_number_pos < number_position:
                second_number = str(numbers.index(number) + 1)
                second_number_pos = number_position

        if second_number is None:
            second_number = first_number

        print(line, first_number, second_number)
        result += int(first_number + second_number)

    return str(result)