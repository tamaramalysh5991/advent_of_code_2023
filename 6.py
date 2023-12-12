
"""
Time:      7  15   30
Distance:  9  40  200
"""

"""
Time:        44     80     65     72
Distance:   208   1581   1050   1102

"""

import math


def solution():
    races = [(44_80_65_72, 208_1581_1050_1102)]
    total_res = []
    for r in races:
        time, distance = r
        start_sec_button = 0
        result = 0
        while start_sec_button <= time:
            speed = start_sec_button
            remainig_sec = time - start_sec_button
            total_distance = speed * remainig_sec
            if total_distance > distance:
                result += 1
            start_sec_button += 1

        print(result)
        total_res.append(result)

    print(math.prod(total_res))


solution()
