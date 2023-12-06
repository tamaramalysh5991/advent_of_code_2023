from utils import get_input


def solution():
    lines = get_input("inputs/4.txt")
    result = []
    for line in lines:
        winning_numbers, numbers = line.split('|')
        winning_numbers = set([w for w in winning_numbers.split(' ') if w.isdigit()])
        numbers = set([n for n in numbers.split(' ') if n.isdigit()])

        found_win_numbers = list(numbers.intersection(winning_numbers))
        if found_win_numbers:
            result.append(2**(len(found_win_numbers)-1))

    return sum(result)


print(solution())


def solution2():
    lines = get_input("inputs/4.txt")
    result = [1] * len(lines)
    for idx, line in enumerate(lines):
        winning_numbers, numbers = line.split('|')
        winning_numbers = set([w for w in winning_numbers.split(' ') if w.isdigit()])
        numbers = set([n for n in numbers.split(' ') if n.isdigit()])

        score = len(list(numbers.intersection(winning_numbers)))
        for i in range(1, score+1):
            result[idx+i] += result[idx]

    return sum(result)


print(solution2())