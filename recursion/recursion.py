from typing import Any


def box_unpacking(box: list[Any]) -> str | None:
    for item in box:
        if isinstance(item, list):
            box_unpacking(item)
        if item == "key":
            print("I found the key.")
            return


def factorial(num: int) -> int:
    if num == 1:
        return 1
    return num * factorial(num - 1)


if __name__ == "__main__":
    box: list[Any] = ["boneca", "carrinho", "lapis", [1, 2, 3], [["key"], 0]]
    box_unpacking(box)
    print(factorial(5))
