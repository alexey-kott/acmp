from typing import List


class Dot:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self. z = z


class Polygon:
    def __init__(self, origin: Dot, vectors: List):
        self.origin = origin
        self.vectors = vectors

    @classmethod
    def read_polygon(cls, file):
        x, y, z = map(int, file.readline().strip().split(" "))
        origin = Dot(x, y, z)

        vectors = []
        for i in range(3):
            vector = map(int, file.readline().strip().split(" "))
            vectors.append(vector)

        return Polygon(origin, vectors)


def main():
    with open("input.txt") as file:
        polygon1 = Polygon.read_polygon(file)
        polygon2 = Polygon.read_polygon(file)


if __name__ == "__main__":
    main()
