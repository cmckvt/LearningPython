class Point:
    __match_args__ = ('x', 'y')		# Preserves args regardless of the order
    def __init__(self, x, y):
        self.x = x
        self.y = y

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

where_is([])
where_is([Point(0, 0)])
where_is([Point(1, 0)])
where_is([Point(0, 1), Point(0, 3)])
where_is([Point(1, 1), Point(2, 3)])

var = 6

where_is([Point(7, var)])		# Single point 7, 6
where_is([Point(9, y=var)])		# Single point 9, 6
where_is([Point(x=11, y=var)])	# Single point 11, 6
where_is([Point(y=var, x=13)])	# Single point 13, 6

where_is([Point(7, 7)])			# Y=X at 7