# Demonstrate the usage of namdtuple objects

import collections


# TODO: create a Point namedtuple
point = collections.namedtuple("point", "x y")
p1 = point(10,20)
p2 = point(30,40)
print(p1, p2)
print(p1.x, p1.y)


# TODO: use _replace to create a new instance
p1 = p1._replace(x=100)
print(p1.x, p1.y)