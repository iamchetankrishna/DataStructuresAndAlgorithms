def binary_search(array, low, high, x):
    if high >= low:
        mid = low + (high - low) // 2
        print(f"Mid : {mid}")
        if array[mid] == x:
            return mid;
        elif array[mid] > x:
            return binary_search(array, low, mid - 1, x)
        else:
            return binary_search(array, mid + 1, high, x)
    return -1


def print_array(arr):
    length_of_array = len(arr)
    for index in range(0, length_of_array):
        print(arr[index], end=" ")
    print()


array = [10, 22, 25, 36, 42, 54, 67, 89, 91, 99]
print_array(array)
returned_index = binary_search(array, 0, len(array), 99)
print(f"Found at index {returned_index}")