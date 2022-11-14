# static methods
class Math:

    @staticmethod
    def add(x, y):
        return x+y

    @staticmethod
    def add5(n):
        return n+5

    @staticmethod
    def add20(n):
        return n + 20

    @staticmethod
    def pi():
        return Math.pi


x = Math.add(5, 258)
y = Math.add5(x)
z = Math.add20(y)
print(x, y, z)
