# Classes Example


# Create some classes and objects

class Shape:
    """Represents a 2-dimensional polygon

    Attributes:
        num_sides: An integer count of the sides
        side_length: A float of side length
    """

    def __init__(self):
        """Creates a new shape with default values."""
        self.num_sides = 4
        self.side_length = 10.0

    def area(self) -> float:
        """Return the area of a square."""
        return self.side_length ** 2

    def perimeter(self) -> float:
        """Return the perimeter of the square"""
        return self.side_length * 4
# TODO: do this on your own

some_shape = Shape()
print(some_shape.area())
print(some_shape.perimeter())

# TODO: call the function and print out the results
