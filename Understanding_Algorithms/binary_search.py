# Implementing binary_search algorithm
from typing import Union


def binary_search(item: int, array: list) -> Union[int, None]:
    head = 0
    top = len(array) - 1
    while head <= top:
        middle = (top + head) // 2
        guess = array[middle]
        if item == guess:
            return item
        elif guess > item:
            top = middle - 1
        else:
            head = middle + 1
    return None


if __name__ == "__main__":
    test_array = [0, 1, 2, 3, 4]
    wanted_item = 4
    result = binary_search(wanted_item, test_array)
    print(result)
