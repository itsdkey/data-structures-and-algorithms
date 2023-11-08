from dataclasses import dataclass, field


@dataclass
class Point:
    x: int
    y: int
    radius: int = 0
    visited: bool = False
    neighbors: list["Point"] = field(default_factory=list)

    def __repr__(self):
        return f"Point{self.x, self.y, self.radius}"
