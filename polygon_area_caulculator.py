# Solution to "Build A Polygon Area Calculator Project", 08/06/2025

# INSTRUCTIONS: In this project you will use object oriented programming
# to create a Rectangle class and a Square class. The Square class should
# be a subclass of Rectangle, and inherit its methods and attributes.

# MORE INFO: https://www.freecodecamp.org/learn/scientific-computing-with-python/build-a-polygon-area-calculator-project/build-a-polygon-area-calculator-project



class Rectangle:
    # distinct width and height parameters for rectangle
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # string representation of rectangle
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    # reset rectangle dimensions
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    # methods to be inherited and used by Square class
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        return f"{'*'*self.width}\n"*self.height

    def get_amount_inside(self, other):
        widths = self.width // other.width
        heights = self.height // other.height
        return widths*heights

class Square(Rectangle):
    def __init__(self, side):
        # inherit methods from square class
        super().__init__(side, side)

    # string representation of square (overrides rectangle methods)
    def __str__(self):
        return f'Square(side={self.width})'

    # reset square dimensions (overrides rectangle methods)
    def set_side(self, side):
        self.width = side
        self.height = side
    def set_width(self, width):
        self.set_side(width)
    def set_height(self, height):
        self.set_side(height)