A = 1, 2, 3, 4, 5, 6, 7, 8
type(A)
A
#%%
cities = [
    ("London", "UK", 8_750_000),
    ("Madrid", "Spain", 5_350_000),
    ("Berlin", "Germany", 6_435_323),
]
# %%
cities[2]
# %%
city, country, population = zip(*cities)

# %%
city
#%%
""" block comment """
# slicing always return a new object


l[0:2] = ("a", "b", "c")
l[0:2]
l = [1, 2, 3, 4, 5, 6]
l[5:1:-1]

# %%
import numbers


class Point:
    def __init__(self, x, y):
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self.pt = (x, y)
        else:
            raise TypeError("Point co-ordinates must be real number")

    def __repr__(self):
        return f"Point(x={self.pt[0]}, y={self.pt[1]})"

    def __len__(self):
        return len(self.pt)

    def __getitem__(self, s):
        return self.pt[s]


p1 = Point(5, 10)
x, y = p1
y
# %%
class Polygon:
    def __init__(self, *pts):
        if pts:
            self._pts = [Point(*pt) for pt in pts]
        else:
            seld._pts = []

    def __repr__(self):
        pts_str = ", ".join([str(pt) for pt in self._pts])
        return f"Pollygon({pts_str})"


p = Polygon((0, 0), Point(1, 1))
p
# %%
# making a sequents
class Polygon:
    def __init__(self, *pts):
        if pts:
            self._pts = [Point(*pt) for pt in pts]
        else:
            seld._pts = []

    def __repr__(self):
        pts_str = ", ".join([str(pt) for pt in self._pts])
        return f"Pollygon({pts_str})"

    def __len__(self):
        return len(self._pts)

    def __getitem__(self, s):
        return self._pts[s]

    def __add__(self, other):
        if isinstance(other, Polygon):
            new_pts = self._pts + other._pts
            return Polygon(*new_pts)
        else:
            raise TypeError("can onmly concatinate with other Polygon")


p1 = Polygon((0, 0), (1, 1))
p2 = Polygon((2, 2), (4, 4))
result = p1 + p2
result
# %%
class Squares:
    def __init__(self, length):
        self.i = 0
        self.length = length

    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result


sq = Squares(5)
while True:
    try:
        item = next(sq)
        print(item)
    except StopIteration:
        break

#%%
class Cities:
    def __init__(self):
        self._cities = [
            "Paris",
            "Berlin",
            "Rome",
            "Belgrade",
            "Madrid",
            "Amsterdam",
            "London",
            "Tokyo",
        ]
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._cities):
            raise StopIteration
        else:
            item = self._cities[self._index]
            self._index += 1
            return item


# %%
class Cities:
    def __init__(self):
        self._cities = [
            "Paris",
            "Berlin",
            "Rome",
            "Belgrade",
            "Madrid",
            "Amsterdam",
            "London",
            "Tokyo",
        ]
        self._index = 0

    def __len__(self):
        return len(self._cities)


#%%
# LAZY EVALUATION
import math


class Circle:
    def __init__(self, r):
        self.radius = r
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self._area = None

    @property
    def area(self):
        if self._area is None:
            print("Calculatin Area ...")
            self._area = math.pi * (self.radius ** 2)
        return self._area


c = Circle(3)
# c.radius
c.area

# %%
origins = set()

with open("/home/nenad/Downloads/yob2014.txt") as f:
    rows = f.readlines()
for row in rows:
    origin = row.strip("\n")
    origins.add(origin)

print(origins)
# %%
import math


class FactIter:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        else:
            result = math.factorial(self.i)
            self.i += 1
        return result


# %%
def song():
    print(" line 1 ")
    yield "I`m a lumberjack"
    print(" line 2 ")
    yield "I sleep all night and work all day"


lines = song()
line = next(lines)
line = next(lines)
line = next(lines)
# %%
import math


class FactIter:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        else:
            result = math.factorial(self.i)
            self.i += 1
        return result


fact_iter = FactIter(5)
list(fact_iter)

# %%
class Squares:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return Squares.squares_gen(self.n)

    @staticmethod
    def squares_gen(n):
        for i in range(n):
            yield i ** 2


sq = Squares(5)
a = list(sq)
a
a * 2
# %%
# Pascal  triangle
from math import factorial


def combo(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


# def pascal_list(size):
#     l = [[combo(n,k) for k in range(n+1)] for n in range(size+1)]
#     for row in l:
#         for item in row:
#             pass

# size = 20
size = 5
l = [[combo(n, k) for k in range(n + 1)] for n in range(size + 1)]
[list(row) for row in l]
# %%
