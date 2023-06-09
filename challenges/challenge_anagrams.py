  
def division(array, low, high):
        pivot_index = low
        pivot_value = array[high]

        for j in range(low, high):
          if array[j] <= pivot_value:
            array[pivot_index], array[j] = array[j], array[pivot_index]
            pivot_index += 1

        array[pivot_index], array[high] = array[high], array[pivot_index]

        return pivot_index

def sort(array, low, high):
    if low < high:
     index = division(array, low, high)
     sort(array, low, index - 1)
     sort(array, index + 1, high)


def is_anagram(first_string, second_string):
    first_str = list(first_string.lower())
    second_str = list(second_string.lower())

    sort(first_str, 0, len(first_str) - 1)
    sort(second_str, 0, len(second_str) - 1)

    first = "".join(first_str)
    second = "".join(second_str)

    if not first_string or not second_string:
        return (first, second, False)

    return (first, second, first == second)