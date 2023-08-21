# Implementing binary search with recursion
def recursive_binary_search(array: list, item: int) -> int:
    if len(array) == 0:
        print("Empty array.")
    elif len(array) == 1:
        if array[0] == item:
            print(f"Item {item} found.")
        else:
            print(f"Item {item} didn't find.")
    else:
        head = array[0]
        top = array[-1]
        middle = (top + head) // 2
        guess = array[middle]
        if guess == item:
            print(f"Item {item} found.")
            return item
        elif guess > item:
            new_array = array[:guess]
            recursive_binary_search(new_array, item)
        else:
            new_array = array[guess:]
            recursive_binary_search(new_array, item)


if __name__ == "__main__":
    test_array = [0, 1, 2, 3]
    recursive_binary_search(test_array, 1)
