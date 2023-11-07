from collections import defaultdict
from math import sqrt
from typing import Any


class Quadrocopter:
    def __init__(
        self, antennas: list[tuple], start: tuple, end: tuple, debug: bool = False
    ) -> None:
        self.debug = debug
        self.antennas = {(x, y): r for x, y, r in antennas}
        self.visited_points = {(x, y): False for x, y, _ in antennas}
        self.connected_antennas = self._group_touching_antennas(antennas)
        self.start = start
        self.end = end

    def _group_touching_antennas(
        self, antennas: list[tuple]
    ) -> defaultdict[tuple, list]:
        groups = defaultdict(list)
        for index, antenna_a in enumerate(antennas):
            *point_a, ra = antenna_a
            for antenna_b in antennas[index + 1 :]:
                *point_b, rb = antenna_b
                line_length = self._get_line_length(antenna_a, antenna_b)
                if line_length <= ra + rb:
                    point_a = tuple(point_a)
                    point_b = tuple(point_b)
                    groups[point_a].append(point_b)
                    groups[point_b].append(point_a)

        self._print(groups)
        return groups

    def _print(self, message: Any) -> None:
        if self.debug:
            print(message)

    @staticmethod
    def _get_line_length(a: tuple, b: tuple) -> float:
        xa, ya, *args = a
        xb, yb, *args = b
        line_length = sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
        return abs(line_length)

    def calculate(self) -> str:
        results = {
            False: "bezpieczny przelot nie jest możliwy",
            True: "bezpieczny przelot jest możliwy",
        }
        result = False
        for point, connections in self.connected_antennas.items():
            line_length = self._get_line_length(self.start, point)
            if line_length <= self.antennas[point]:
                if result := self._calculate(point, connections):
                    break
        return results[result]

    def _calculate(self, point: tuple, connections: [list[tuple]]) -> bool:
        found_path = False
        self._print(f"visiting: {point}, neighbors: {connections}")
        self.visited_points[point] = True

        line_length = self._get_line_length(self.end, point)
        self._print(f"{line_length=}")
        if line_length <= self.antennas[point]:
            self._print("Found end point.")
            return True

        for neighbor in connections:
            if not self.visited_points[neighbor]:
                return self._calculate(neighbor, self.connected_antennas[neighbor])
        return found_path
