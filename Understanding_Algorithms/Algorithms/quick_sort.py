import random

# Implementing quick sort algorithm


def quick_sort(array: list) -> list:
    if len(array) < 2:
        return array
    rand_index = random.randrange(len(array))
    pivot = array[rand_index]
    less_than_pivot = [ele for ele in array if ele < pivot]
    greater_than_pivot = [ele for ele in array if ele > pivot]
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


if __name__ == "__main__":
    test_array = [3, 1, 4, 2, 5, 9, 7, 0, 8]
    print(quick_sort(test_array))
