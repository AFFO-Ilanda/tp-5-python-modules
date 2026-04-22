import math

class Point3D:
    Npts = 0
    Mx = None
    My = None
    Mz = None

    def __init__(self, x, y, z):
        self.__x = x
        self.__y = y
        self.__z = z
        Point3D.Npts += 1
        Point3D.Mx = x if Point3D.Mx is None else max(Point3D.Mx, x)
        Point3D.My = y if Point3D.My is None else max(Point3D.My, y)
        Point3D.Mz = z if Point3D.Mz is None else max(Point3D.Mz, z)

    @classmethod
    def getNpts(cls):
        return cls.Npts

    @classmethod
    def getMaxX(cls):
        return cls.Mx

    @classmethod
    def getMaxY(cls):
        return cls.My

    @classmethod
    def getMaxZ(cls):
        return cls.Mz

    def __repr__(self):
        return f"Point3D({self.__x}, {self.__y}, {self.__z})"

    def __str__(self):
        return f"Point3D(x={self.__x}, y={self.__y}, z={self.__z})"

    @staticmethod
    def estSurDiagonale(x, y, z):
        return x == y == z



a3D = Point3D(1, 2, 3)
b3D = Point3D(5, 5, 5)
c3D = Point3D(4, 7, 2)

try:
    print(a3D.__x)
except AttributeError as e:
    print(f"Accès refusé : {e}")

print(f"\nNombre de points créés : {Point3D.getNpts()}")
print(f"Max X : {Point3D.getMaxX()}")
print(f"Max Y : {Point3D.getMaxY()}")
print(f"Max Z : {Point3D.getMaxZ()}")

print(f"\n{a3D}")
print(f"repr(b3D) → {repr(b3D)}")
b3D_copie = eval(repr(b3D))
print(f"Copie reconstruite : {b3D_copie}")

print(f"\nb3D sur la diagonale ? {Point3D.estSurDiagonale(5, 5, 5)}")   # True
print(f"a3D sur la diagonale ? {Point3D.estSurDiagonale(1, 2, 3)}")    # False