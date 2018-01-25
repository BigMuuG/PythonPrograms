import random


def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + \
            self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __lt__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum < secondnum

    def __gt__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num

        return firstnum > secondnum

    def __mul__(self, other):
        divi = gcd(self.den, other.den)
        nnum = (self.num * other.num) // divi
        nden = (self.den * other.den) // divi

        return Fraction(nnum, nden)

    def __floordiv__(self, other):
        divi = gcd(self.den, other.den)
        nnum = (self.num * other.den) // divi
        nden = (self.den * other.num) // divi

        return Fraction(nnum, nden)


rArray = [random.randint(1, 10) for i in range(10)]
x = Fraction(rArray[0], rArray[1])
y = Fraction(rArray[2], rArray[3])
print(x)
print(y)
print(x + y)
print(x == y)
print(x * y)
print(x // y)
print(x > y)
print(x < y)
