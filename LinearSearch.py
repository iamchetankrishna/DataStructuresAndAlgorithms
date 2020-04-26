def linear_search(arr, x):
    length_of_array = len(arr)
    number_of_iterations = 0
    for index in range(0, length_of_array):
        number_of_iterations = number_of_iterations + 1
        if x == arr[index]:
            return index, number_of_iterations
    return -1, number_of_iterations


def print_array(arr):
    length_of_array = len(arr)
    for index in range(0, length_of_array):
        print(arr[index], end=" ")
    print()


array = [10, 17, 2, 78, 39, 43, 1, 45, 10, 99]
print_array(array)
return_index, number_of_iterations = linear_search(array, 101)
print(f"Element found at {return_index} : Total Number of Iteration {number_of_iterations}")
