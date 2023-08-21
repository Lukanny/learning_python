from Understanding_Algorithms.Algorithms.selection_sort import find_smaller


# Function that finds the biggest array number in a array recursively
def recursive_find_greater_item(array: list) -> int:
    if len(array) == 0:
        greater_item = 0
        return greater_item
    elif len(array) == 1:
        greater_item = array[0]
        return greater_item
    else:
        smaller = find_smaller(array)
        array.pop(smaller)
        greater_item = recursive_find_greater_item(array)
        return greater_item


if __name__ == "__main__":
    test_array = [0, 4, 1, 3, 2, 7]
    print(recursive_find_greater_item(test_array))
