"""
    Given the participants' score sheet for your University Sports Day, you are required
    to find the runner-up score. You are given  scores. Store them in a list and find the
    score of the runner-up.

    Input Format

    The first line contains . The second line contains an array   of  integers each separated
    by a space.
"""

arr = [2, 3, 6, 6, 5]


def selection_sort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j

        # swap
        temp = array[i]
        array[i] = array[min_idx]
        array[min_idx] = temp

    return array


def search(array, value):
    ind = []
    for i, x in enumerate(array):
        if x == value:
            ind.append(i)

    return ind


def searching_runner_up(array, index_list):
    index = index_list[0]
    last = array[0]
    for i in range(index):
        last = array[i]

    return last


arr_sort = selection_sort(arr)
list_index = search(arr_sort, arr_sort[-1])
searching_runner_up(arr_sort, list_index)
