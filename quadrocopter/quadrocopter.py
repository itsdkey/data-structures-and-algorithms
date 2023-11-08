from math import sqrt
from typing import Any

from .dataclasses import Point


class Quadrocopter:
    def __init__(
        self, antennas: list[Point], start: Point, end: Point, debug: bool = False
    ) -> None:
        self.debug = debug
        self.antennas = self._find_neighbors(antennas)
        self.start = start
        self.end = end

    def _print(self, message: Any) -> None:
        if self.debug:
            print(message)

    def _find_neighbors(self, antennas: list[Point]) -> list[Point]:
        for index, antenna_a in enumerate(antennas):
            for antenna_b in antennas[index + 1 :]:
                line_length = self._get_line_length(antenna_a, antenna_b)
                if line_length <= antenna_a.radius + antenna_b.radius:
                    antenna_a.neighbors.append(antenna_b)
                    antenna_b.neighbors.append(antenna_a)
        return antennas

    @staticmethod
    def _get_line_length(a: Point, b: Point) -> float:
        line_length = sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)
        return abs(line_length)

    def calculate(self) -> str:
        results = {
            False: "bezpieczny przelot nie jest możliwy",
            True: "bezpieczny przelot jest możliwy",
        }
        result = False
        for point in self.antennas:
            line_length = self._get_line_length(self.start, point)
            if line_length <= point.radius:
                if result := self._calculate(point):
                    break
        return results[result]

    def _calculate(self, point: Point) -> bool:
        self._print(f"visiting: ({point.x, point.y}), neighbors: {point.neighbors}")
        point.visited = True
        line_length = self._get_line_length(self.end, point)
        self._print(f"{line_length=}")
        if line_length <= point.radius:
            self._print("found end point.")
            return True

        found_path = False
        for neighbor in point.neighbors:
            if not neighbor.visited:
                return self._calculate(neighbor)
        return found_path
