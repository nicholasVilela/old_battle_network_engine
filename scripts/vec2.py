class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def as_tuple(self):
        return (self.x, self.y)

    def set(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, vec2):
        return self.x == vec2.x and self.y == vec2.y

    def __add__(self, vec2):
        target_vec = (self.x + vec2.x, self.y + vec2.y)

        return Vec2(target_vec[0], target_vec[1])

    def __sub__(self, vec2): 
        target_vec = (self.x - vec2.x, self.y - vec2.y)

        return Vec2(target_vec[0], target_vec[1])

    def add_with(self, val: int):
        target_vec = (self.x + val, self.y + val)

        return Vec2(target_vec[0], target_vec[1])

    def mul_with(self, val):
        target_vec = (self.x * val, self.y * val)

        return Vec2(target_vec[0], target_vec[1])

    def div_with(self, val):
        if val != 0:
            target_vec = (self.x / val, self.y / val)

            return Vec2(target_vec[0], target_vec[1])
        
        return self