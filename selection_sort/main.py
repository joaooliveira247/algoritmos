def find_smallest(arr: list[int]) -> int:
    smallest: int = arr[0]
    smallest_index: int = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr: list[int]) -> list[int]:
    new_arr: list[int] = []
    for _ in range(len(arr)):
        smallest: int = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


print(selection_sort([5, 3, 6, 2, 10]))
