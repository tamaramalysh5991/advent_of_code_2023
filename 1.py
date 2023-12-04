# https://adventofcode.com/2023/day/1


# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet

from utils import get_input


def get_sum_of_all_calibration_values_part_1() -> int:
    lines = get_input("inputs/1.txt")
    result = []
    for line in lines:
        digits = [l for l in line if l.isdigit()]
        result.append(int("".join([digits[0], digits[-1]])))
    return sum(result)


def get_sum_of_all_calibration_values_part_2():
    """
    numbers_str_to_val = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }
    """
    numbers_str_to_val = {
        **{
            n_str: n_val
            for (n_val, n_str) in enumerate(
                "one two three four five six seven eight nine".split(), start=1
            )
        },
        **{str(i + 1): i + 1 for i in range(9)},
    }
    max_length = len(max(numbers_str_to_val.keys(), key=len))
    lines = get_input("inputs/1.txt")
    result = 0
    for line in lines:
        numbers = []
        for i in range(len(line)):
            for number in numbers_str_to_val.keys():
                if line[i : i + max_length :].find(str(number)) == 0:
                    numbers.append(numbers_str_to_val[number])
        if numbers:
            result += int(str(numbers[0]) + str(numbers[-1]))
    return result


print(get_sum_of_all_calibration_values_part_2())
