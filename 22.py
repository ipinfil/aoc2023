from typing import List

RED_COUNT = 12
GREEN_COUNT = 13
BLUE_COUNT = 14

def solve(data: List[str]):
    power_sum = 0
    for line in data:
        game_parts = line[line.find(':') + 2:].split(';')
        needed_red = 0
        needed_green = 0
        needed_blue = 0

        for game_part in game_parts:
            color_balls = game_part.split(',')
            red_sum = 0
            green_sum = 0
            blue_sum = 0

            for color_ball in color_balls:
                color_ball = color_ball.strip()
                if 'blue' in color_ball:
                    blue_sum += int(color_ball.split(' ')[0])
                elif 'green' in color_ball:
                    green_sum += int(color_ball.split(' ')[0])
                elif 'red' in color_ball:
                    red_sum += int(color_ball.split(' ')[0])

            if needed_red is None or needed_red < red_sum:
                needed_red = red_sum
            if needed_green is None or needed_green < green_sum:
                needed_green = green_sum
            if needed_blue is None or needed_blue < blue_sum:
                needed_blue = blue_sum

        print(line)
        print('red:', needed_red, 'green:', needed_green, 'blue:', needed_blue)
        print('---')
        power_sum += needed_red * needed_green * needed_blue

    return power_sum