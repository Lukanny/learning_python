# Function that sums all numbers in a array recursively

def recursive_array_sum(array: list) -> int:
    if len(array) == 0:
        sum_array = 0
        return sum_array
    elif len(array) == 1:
        sum_array = array[0]
        return sum_array
    else:
        sum_array = array.pop(-1)
        return sum_array + recursive_array_sum(array)


if __name__ == "__main__":
    test_array = []
    print(recursive_array_sum(test_array))
