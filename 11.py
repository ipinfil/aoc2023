def solve(data: list) -> str:
    result = 0

    for line in data:
        first_number = None
        second_number = None

        for char in line:
            if char.isdigit():
                if first_number is None:
                    first_number = char
                else:
                    second_number = char

        if second_number is None:
            second_number = first_number
        result += int(first_number + second_number)

    return str(result)