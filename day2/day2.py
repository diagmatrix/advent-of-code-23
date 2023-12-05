import re

RED = 12
GREEN = 13
BLUE = 14

problem_input = open("input.txt", "r").readlines()  # Add input.txt in the directory

total_possible = 0
total_power = 0
for game_id, game_raw in enumerate(problem_input):
    game = re.sub(r'Game \d+: ', '', game_raw).strip('\n').split(';')
    valid_game = True
    max_red, max_green, max_blue = 0, 0, 0
    for cubes_shown_raw in game:
        red, green, blue = 0, 0, 0
        cubes_shown = cubes_shown_raw.lstrip().split(',')
        for cubes in cubes_shown:
            cube_data = cubes.lstrip().split(' ')
            match cube_data[1]:
                case "red":
                    num = int(cube_data[0])
                    red += num
                    if num > max_red:
                        max_red = num
                case "green":
                    num = int(cube_data[0])
                    green += num
                    if num > max_green:
                        max_green = num
                case "blue":
                    num = int(cube_data[0])
                    blue += num
                    if num > max_blue:
                        max_blue = num
        if red > RED or green > GREEN or blue > BLUE:
            valid_game = False

    if valid_game:
        total_possible += game_id + 1
    total_power += max_red*max_green*max_blue

print(f'Sum of possible games: {total_possible}')
print(f'Power of cubes: {total_power}')
