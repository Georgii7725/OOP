def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

class Frac:
    def __init__(self, m, n=1) -> None:
        if n == 0:
            self.m = m
            self.n = 1
        else:
            self.m = m * n // abs(n)
            self.n = abs(n)
        self.simplify()
    
    def __str__(self) -> str:
        if self.m == 0:
            return "0"
        if self.n == 1:
            return str(self.m)
        return f"{self.m}/{self.n}"

    def simplify(self) -> None:
        k = gcd(abs(self.m), abs(self.n))
        self.m //= k
        self.n //= k 
    
    
    ################################## Сложение #############################################
    def __add__(self, other):
        if isinstance(other, int):
            other = Frac(other)
        ans = Frac(self.m * other.n + other.m * self.n, self.n * other.n)
        ans.simplify()
        return ans
    
    def __radd__(self, other):
        return self + other

    ################################## Вычитание #############################################
    def __neg__(self):
        return Frac(-self.m, self.n)
    
    def __sub__(self, other):
        if isinstance(other, int):
            other = Frac(other)
        ans = self + (-other)
        return ans
    
    def __rsub__(self, other):
        if isinstance(other, int):
            other = Frac(other)
        return other - self
    
    ################################## Произведение #############################################   
    def __mul__(self, other):
        if isinstance(other, int):
            other = Frac(other)
        ans = Frac(self.m*other.m, self.n*other.n)
        ans.simplify()
        return ans
    
    def __rmul__(self, other):
        return self*other
    
    ################################## Деление #############################################
    def __invert__(self):
        return Frac(self.n, self.m)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Frac(other) if other != 0 else Frac(1)
        return self * (~other)
    
    def __rtruediv__(self, other):
        if isinstance(other, int):
            other = Frac(other)
        return other / self

    ################################## Возведение в степень #############################################
    def __pow__(self, other):
        ans = 1
        for _ in range(other):
            ans = ans * self
        return ans
