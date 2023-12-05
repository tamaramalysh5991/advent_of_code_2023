# https://adventofcode.com/2023/day/2
import re

from utils import get_input

# only 12 red cubes, 13 green cubes, and 14 blue cubes
rules = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def _help_func(result, game_id, game_res):
    for color in rules.keys():
        if game_res[color] > rules[color]:
            return result
    result += int(game_id)
    return result


def get_solution():
    lines = get_input("inputs/2.txt")

    result = 0
    result2 = 0
    game_pattern = r"Game (\d+)"
    for line in lines:
        game_id = re.findall(game_pattern, line, re.DOTALL)[0]
        color_number_pairs = re.findall(r"(\d+)\s*(blue|red|green)", line)
        game_res = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for number, color in color_number_pairs:
            game_res[color] = max(game_res[color], int(number))

        result = _help_func(result=result, game_id=game_id, game_res=game_res)
        power = game_res["red"] * game_res["green"] * game_res["blue"]
        result2 += power

    return result, result2


print(get_solution())
