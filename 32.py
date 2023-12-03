from typing import List


def solve(data: List[str]):
    last_number = None
    last_number_positions = []
    adjacent_symbol_numbers = {}

    for i, row in enumerate(data):
        for j, symbol in enumerate(row):
            if symbol.isdigit():
                last_number_positions.append((i, j))
                if last_number is None:
                    last_number = symbol
                else:
                    last_number += symbol

            if not symbol.isdigit() or j == len(row) - 1:
                if last_number is None:
                    continue

                adjacent_symbol = get_adjacent_symbol(last_number_positions, data)
                if adjacent_symbol:
                    if adjacent_symbol[1] not in adjacent_symbol_numbers:
                        adjacent_symbol_numbers[adjacent_symbol[1]] = []

                    adjacent_symbol_numbers[adjacent_symbol[1]].append(int(last_number))
                last_number = None
                last_number_positions = []
                continue

    result = 0
    for symbol in adjacent_symbol_numbers:
        if data[symbol[0]][symbol[1]] != '*' or len(adjacent_symbol_numbers[symbol]) < 2:
            continue

        game_result = None
        for number in adjacent_symbol_numbers[symbol]:
            if game_result is None:
                game_result = number
            else:
                game_result *= number

        result += game_result


    return result

def get_adjacent_symbol(positions: List[tuple], map: List[str]) -> tuple:
    for i, j in positions:
        if i > 0 and map[i - 1][j] != '.' and not map[i-1][j].isdigit():
            return (map[i - 1][j], (i - 1, j))
        if i < len(map) - 1 and map[i + 1][j] != '.' and not map[i+1][j].isdigit():
            return (map[i + 1][j], (i + 1, j))
        if j > 0 and map[i][j - 1] != '.' and not map[i][j-1].isdigit():
            return (map[i][j - 1], (i, j - 1))
        if j < len(map[0]) - 1 and map[i][j + 1] != '.' and not map[i][j+1].isdigit():
            return (map[i][j + 1], (i, j + 1))

        #diagonal
        if i > 0 and j > 0 and map[i - 1][j - 1] != '.' and not map[i-1][j-1].isdigit():
            return (map[i - 1][j - 1], (i - 1, j - 1))
        if i > 0 and j < len(map[0]) - 1 and map[i - 1][j + 1] != '.' and not map[i-1][j+1].isdigit():
            return (map[i - 1][j + 1], (i - 1, j + 1))
        if i < len(map) - 1 and j > 0 and map[i + 1][j - 1] != '.' and not map[i+1][j-1].isdigit():
            return (map[i + 1][j - 1], (i + 1, j - 1))
        if i < len(map) - 1 and j < len(map[0]) - 1 and map[i + 1][j + 1] != '.' and not map[i+1][j+1].isdigit():
            return (map[i + 1][j + 1], (i + 1, j + 1))
    return None