from .dataclasses import Point
from .quadrocopter import Quadrocopter


def get_antennas() -> list[Point]:
    """Collect antennas.

    An antenna has information: (x, y, radius/power).
    """
    number = int(input())
    results = []
    for i in range(number):
        x, y, radius = tuple(int(x) for x in input().split(" "))
        results.append(Point(x, y, radius))
    return results


def get_start_end() -> tuple[Point, Point]:
    start_point = Point(*tuple(int(x) for x in input().split(" ")))
    end_point = Point(*tuple(int(x) for x in input().split(" ")))
    return start_point, end_point


if __name__ == "__main__":
    antennas = get_antennas()
    start, end = get_start_end()
    result = Quadrocopter(antennas, start, end).calculate()
    print(result)
