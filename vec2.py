import math


class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def norm(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def normalize(self):
        n = self.norm()
        if n != 0:
            return Vec2(self.x/n, self.y/n)
        raise ZeroDivisionError("vector has length zero")

    def rot90(self):
        return Vec2(self.y, -self.x)
    
    def rot270(self):
        vec = self
        for i in range(0, 2):
            vec = vec.rot90()
            
    def __repr__(self):
        return f"Vec2({self.x}, {self.y})"

    def __eq__(self, vec):
        return self.x == vec.x and self.y == vec.y
            
    def __add__(self, vec):
        if isinstance(vec, Vec2):
            return Vec2(self.x + vec.x, self.y + vec.y)
        return Vec2(self.x + vec, self.y + vec)
    
    def __radd__(self, n):
        return Vec2(self.x + n, self.y + n)
    
    def __sub__(self, vec):
        if isinstance(vec, Vec2):
            return Vec2(self.x - vec.x, self.y - vec.y)
        return Vec2(self.x - vec, self.y - vec)
    
    def __mul__(self, n):
        if isinstance(n, Vec2):
            raise ValueError("no vector to vector multiplication")
        return Vec2(self.x*n, self.y*n)
    
    def __rmul__(self, n):
        return self*n
    
    def __truediv__(self, n):
        return Vec2(self.x/n, self.y/n)
    
    def __getitem__(self, idx):
        vec = [self.x, self.y]
        if idx > 1 or idx < -2:
            raise IndexError("vector only has two dimensions")
        return vec[idx]
    
    def __setitem__(self, idx, val):
        if idx > 1 or idx < -2:
            raise IndexError("vector only has two dimensions")
        if idx == -2:
            self.x = val
        elif idx == -1:
            self.y = val
        elif idx == 0:
            self.x = val
        elif idx == 1:
            self.y = val
