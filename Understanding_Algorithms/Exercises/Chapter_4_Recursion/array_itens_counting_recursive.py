# Function that counts numbers in a array recursively

def recursive_array_itens_counting(array: list) -> int:
    if len(array) == 0:
        count = 0
        return count
    elif len(array) == 1:
        count = 1
        return count
    else:
        if array.pop(-1):
            count = 1
            return count + recursive_array_itens_counting(array)


if __name__ == "__main__":
    test_array = [0, 1, 2]
    print(recursive_array_itens_counting(test_array))
