def quicksort(array):
    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    return quicksort(left) + middle + quicksort(right)


def is_anagram(first_string, second_string):
    first_str = list(first_string.lower())
    second_str = list(second_string.lower())

    sorted_first = quicksort(first_str)
    sorted_second = quicksort(second_str)

    first = "".join(sorted_first)
    second = "".join(sorted_second)

    if not first_string or not second_string:
        return (first, second, False)

    return (first, second, first == second)