from typing import List


def solve(data: List[str]):
    result = 0
    last_number = None
    last_number_positions = []
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

                if len(last_number_positions) > 0 and has_adjacent_symbol(last_number_positions, data):
                    result += int(last_number)

                last_number = None
                last_number_positions = []
                continue

    return result

def has_adjacent_symbol(positions: List[tuple], map: List[str]) -> bool:
    for i, j in positions:
        if i > 0 and map[i - 1][j] != '.' and not map[i-1][j].isdigit():
            return True
        if i < len(map) - 1 and map[i + 1][j] != '.' and not map[i+1][j].isdigit():
            return True
        if j > 0 and map[i][j - 1] != '.' and not map[i][j-1].isdigit():
            return True
        if j < len(map[0]) - 1 and map[i][j + 1] != '.' and not map[i][j+1].isdigit():
            return True

        #diagonal
        if i > 0 and j > 0 and map[i - 1][j - 1] != '.' and not map[i-1][j-1].isdigit():
            return True
        if i > 0 and j < len(map[0]) - 1 and map[i - 1][j + 1] != '.' and not map[i-1][j+1].isdigit():
            return True
        if i < len(map) - 1 and j > 0 and map[i + 1][j - 1] != '.' and not map[i+1][j-1].isdigit():
            return True
        if i < len(map) - 1 and j < len(map[0]) - 1 and map[i + 1][j + 1] != '.' and not map[i+1][j+1].isdigit():
            return True
    return False