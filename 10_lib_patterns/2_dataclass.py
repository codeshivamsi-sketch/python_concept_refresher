from dataclasses import dataclass
# Lighter alternative to pydantic, No validation.

@dataclass
class Point:
    x: float
    y: float = 1 # default value

p = Point(1.2, 2.4)
print(p.x)
print(p)