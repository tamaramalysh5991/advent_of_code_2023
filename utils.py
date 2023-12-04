from typing import List


def get_input(file_name: str) -> List[str]:
    with open(file_name) as f:
        data = f.read().splitlines()
    return data
