import math

def teilor(a):
        f = math.factorial
        return a**3/f(3)-a**5/f(5)+a**7/f(7)-a**9/f(9)+a**11/f(11)

def geron(a,b,c):
    p = (a + b + c) /2
    return (p*(p-a)*(p-b)*(p-c))**0.5

# Коордианты хранятся в декартовой системе координат
class Point:
    # Констуктор для оконных СК 
    def __init__(self, x, y, root=None) -> None:
        if root is not None:
            self.x = x + root.winfo_width() / 2
            self.y = root.winfo_height() / 2 - y
        else:
            self.x = x
            self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, p):
        return Point(self.x+p.x, self.y+p.y)
    
    def __sub__(self, p):
        return Point(self.x-p.x, self.y-p.y)
    
    def module(self) -> float:
        return (self.x**2 + self.y**2)**0.5
    
    def distanceTo(self, p) -> float:
        return (self-p).module() if isinstance(p, Point) else None

# A - нижняя левая точка, B - верхняя правая
class Rectangle:
    def __init__(self, A, B=None, width=None, height=None) -> None:
        if B is not None:
            self.A = Point(min(A.x, B.x), min(A.y, B.y))
            self.B = Point(max(A.x, B.x), max(A.y, B.y))
        elif width is not None and height is not None: 
            self.A = A
            self.B = A + Point(width, height)
        else:
            self.A, self.B = A, A
    
    def __str__(self) -> str:
        return f"{self.A} -> {self.B}\n"

    def area(self) -> float:
        shift = self.B - self.A
        return shift.x * shift.y
    
    def perimeter(self) -> float:
        shift = self.B - self.A
        return 2*(shift.x + shift.y)
    
    def intersection_area_with(self, P) -> float:
        return Rectangle(A=Point(
                            max(self.A.x, P.A.x),
                            max(self.A.y, P.A.y)
                            ), 
                        B=Point(
                            min(self.B.x, P.B.x),
                            min(self.B.y, P.B.y)
                            )
                        ).area() if isinstance(P, Rectangle) else None
    
class Circle:
    def __init__(self, P, r) -> None:
        self.P = P
        self.r = abs(r)

    def __str__(self):
        return f"центр {self.P} с R = {self.r}\n"

    def __contains__(B, A) -> bool:
        return B.P.distanceTo(A.P) + A.r <= B.r

    def area(self) -> float:
        return math.pi*self.r**2
    
    def length(self) -> float:
        return 2*math.pi*self.r

    def intersection_area_with(self, C) -> float:
        if self in C: return self.area()
        if C in self: return C.area()

        R = self.r
        r = C.r
        l = self.P.distanceTo(C.P)
        if R + r <= l: return 0
        
        H = 4*geron(R, r, l)/l
        alpha = math.acos((2*R**2-H**2)/(2*R**2))
        betta = math.acos((2*r**2-H**2)/(2*r**2))
        return (R**2*teilor(alpha)+r**2*teilor(betta))/2

print(Rectangle(Point(0,0)).area())
print(Circle(Point(0,0),0).area())

A = Circle(Point(0,0), 1)
B = Circle(Point(2,0), 2)
print(A in B)
print(A.intersection_area_with(B))

A = Circle(Point(0,0), 0)
B = Circle(Point(2,0), 2)
print(A in B)
print(A.intersection_area_with(B))