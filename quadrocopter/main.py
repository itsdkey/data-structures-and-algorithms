from quadrocopter import Quadrocopter


def get_antennas() -> list[tuple]:
    """Collect antennas.

    An antenna has information: (x, y, radius/power).
    """
    number = int()
    results = []
    for i in range(number):
        results.append(tuple(int(x) for x in input().split(" ")))
    return results


def get_start_end() -> tuple[tuple[int], tuple[int]]:
    start_point = tuple(int(x) for x in input().split(" "))
    end_point = tuple(int(x) for x in input().split(" "))
    return start_point, end_point


if __name__ == "__main__":
    antennas = get_antennas()
    start, end = get_start_end()
    result = Quadrocopter(antennas, start, end).calculate()
    print(result)
