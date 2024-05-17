class Point:
    __match_args__ = ('x', 'y')	# ignores the rest of passed in args
    def __init__(self, x, y, *rest):
        self.x = x
        self.y = y
        self.rest = rest

def where_is(point):
    match point:
        case []:
            print("No points")
        case [Point(0, 0)]:
            print("The origin")
        case [Point(x, y)] if x == y:
            print(f"Y=X at {x}")
        case [Point(x, y)]:
            print(f"Single point {x}, {y}")
        case [Point(0, y1), Point(0, y2)]:
            print(f"Two on the Y axis at {y1}, {y2}")
        case _:
            print("Something else")

where_is([Point(0, 0, 6)])
where_is([Point(0, 0, (6, 5))])
where_is([Point(0, 0, [6,7,8])])
where_is([Point(y=0, x=0)])

# SyntaxError: positional argument follows keyword argument
#where_is([Point(y=0, x=0, [6,7,8])])

# This causes a redefinition of X errpr? How to resolve?
# All positional arguments need to come before keyword arguments
# where_is([Point([6,7,8], y=0, x=0)])



