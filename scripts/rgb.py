class RGB:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return f'(R: {self.r}, G: {self.g}, B: {self.b})'

    def __add__(self, other):
        return RGB(
            r=self.r + other.r,
            g=self.g + other.g,
            b=self.b + other.b,
        )

    def __sub__(self, other):
        return RGB(
            r=self.r - other.r,
            g=self.g - other.g,
            b=self.b - other.b,
        )

    def __mul__(self, other):
        return RGB(
            r=self.r * other,
            g=self.g * other,
            b=self.b * other,
        )

    def __truediv__(self, other):
        return RGB(
            r=self.r / other,
            g=self.g / other,
            b=self.b / other,
        )
