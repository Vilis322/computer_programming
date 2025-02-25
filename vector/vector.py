class Vector:
    """Represents a 2D vector.

    Supports addition, subtracting scalar multiplication and reverse multiplication via '*', and string representations.
    """
    def __init__(self, x: float, y: float):
        """Initialize the vector with axis x and y coordinates.

        Args:
            x (float): The x-coordinate of the vector.
            y (float): The y-coordinate of the vector.
        """
        self.x = x
        self.y = y

    def __add__(self, other: "Vector") -> "Vector":
        """Adds two vectors.

        Args:
            other (Vector): The other vector that needs to be added.

        Returns:
            Vector: A new vector that is a result of adding two vectors.

        Raises:
            TypeError: If the other is not an instance of the Vector class.
        """
        try:
            if not isinstance(other, Vector):
                raise TypeError("Operands must be instances of the Vector class.")
        except TypeError as e:
            print(str(e))
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __radd__(self, other: "Vector") -> "Vector":
        """Adds two vectors.

        Args:
            other (Vector): The other vector that needs to be added.

        Returns:
            Vector: A new vector that is a result of adding two vectors.
        """
        return self + other

    def __sub__(self, other: "Vector") -> "Vector":
        """Subtracts one vector from another.

        Args:
            other (Vector): The other vector that needs to be subtracted.

        Returns:
            Vector: A new vector that is a result of subtracting one vector from another.

        Raises:
            TypeError: If the other is not an instance of the Vector class.
        """
        try:
            if not isinstance(other, Vector):
                raise TypeError("Operands must be instances of the Vector class.")
        except TypeError as e:
            print(str(e))
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __rsub__(self, other: "Vector") -> "Vector":
        """Subtracts one vector from another.

        Args:
            other (Vector): The other vector that needs to be subtracted.

        Returns:
            Vector: A new vector that is a result of subtracting one vector from another.
        """
        return self - other

    def __mul__(self, scalar: float) -> "Vector":
        """Multiplies vector on scalar.

        Args:
            scalar (float): The scalar value that needs to multiply by a vector.

        Returns:
            Vector: A new vector that is a result of multiplying by a scalar.

        Raises:
            TypeError: If the scalar is not an instance of the `float` type.
        """
        try:
            if not isinstance(scalar, float):
                raise TypeError("The scalar value must be a numeric value.")
        except TypeError as e:
            print(str(e))
            return NotImplemented
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: float) -> "Vector":
        """Handles scalar multiplication when the scalar is on the left side of the multiplication.

        Args:
            scalar (float): The scalar value that needs to multiply by a vector.

        Returns:
            Vector: A new vector that is a result of multiplying by a scalar.
        """
        return self * scalar

    def __str__(self) -> str:
        """Returns a string representation of the vector."""
        return f"({self.x}, {self.y})"


if __name__ == "__main__":
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    print(v2 + v1)
    print(v1 - v2)
    v3 = v2 + v1
    print(v3)
    print(v2 * 3.5)
    v4 = v2 * 3.5
    print(v4)
    v5 = 3.5 * v2
    print(v5)

    # Test block
    try:
        print(v2 + 1)
    except TypeError as e:
        print(str(e))

    try:
        print(v2 - 1)
    except TypeError as e:
        print(str(e))

    try:
        print(v2 * v1)
    except TypeError as e:
        print(str(e))

    try:
        print(2 - v2)
    except TypeError as e:
        print(str(e))

    try:
        print(2 + v2)
    except TypeError as e:
        print(str(e))
