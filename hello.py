import fire
from random import choices


def add():
    numbers = [6, 5, 21, 30, 50]
    x = choices(numbers)[0]
    y = choices(numbers)[0]
    sum = int(x) + int(y)
    return x, y, sum


# print(f"This is the sum: 1, 2, {result}")

if __name__ == "__main__":
    fire.Fire(add)
