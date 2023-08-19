# Function to find the index of the smaller array item


def find_smaller(array: list) -> int:
    smaller = array[0]
    smaller_index = 0
    for i in range(len(array)):
        if array[i] < smaller:
            smaller = array[i]
            smaller_index = i
    return smaller_index

# Implementing selection sort algorithm


def selection_sort(array: list) -> list:
    sorted_array = []
    for i in range(len(array)):
        smaller = find_smaller(array)
        sorted_array.append(array.pop(smaller))
    return sorted_array


if __name__ == "__main__":
    test_array = [5, 3, 1, 2, 0, 4]
    final_array = selection_sort(test_array)
    print(final_array)
