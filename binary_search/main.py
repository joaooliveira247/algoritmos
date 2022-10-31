def binary_search(list: list[int], item: int) -> None | int:
    low: int = 0
    high: int = len(list) - 1

    while low <= high:
        mid: int = (low + high) // 2
        guess: int = list[mid]
        match guess:
            case _ if guess == item:
                return mid
            case _ if guess > item:
                high = mid - 1
            case _:
                low = mid + 1

    return None


if __name__ == "__main__":
    my_list = [1, 3, 5, 7, 9]
    print(binary_search(my_list, 3))
    print(binary_search(my_list, -1))
