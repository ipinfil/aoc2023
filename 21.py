from typing import List

RED_COUNT = 12
GREEN_COUNT = 13
BLUE_COUNT = 14

def solve(data: List[str]):
    game_id_sum = 0
    for line in data:
        game_id = line[5:line.find(':')]
        game_parts = line[line.find(':') + 2:].split(';')
        ok = True

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

            if red_sum > RED_COUNT or green_sum > GREEN_COUNT or blue_sum > BLUE_COUNT:
                ok = False
                break

        print(line)
        print('red:', red_sum, 'green:', green_sum, 'blue:', blue_sum, 'ok:', red_sum <= RED_COUNT and green_sum <= GREEN_COUNT and blue_sum <= BLUE_COUNT)
        if ok:
            print(f'****************** + {game_id} ******************')
            game_id_sum += int(game_id)
        print('---')
    return game_id_sum