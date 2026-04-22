class Rectangle:
    Nrect = 0
    MaxSurface = 0.0

    def __init__(self, largeur, hauteur):
        self.__largeur = largeur
        self.__hauteur = hauteur
        Rectangle.Nrect += 1
        surface = largeur * hauteur
        if surface > Rectangle.MaxSurface:
            Rectangle.MaxSurface = surface

    @classmethod
    def getNrect(cls):
        return cls.Nrect

    @classmethod
    def getMaxSurface(cls):
        return cls.MaxSurface

    def __repr__(self):
        return f"Rectangle({self.__largeur}, {self.__hauteur})"

    def __str__(self):
        surface = self.__largeur * self.__hauteur
        return (f"Rectangle — largeur : {self.__largeur}, "
                f"hauteur : {self.__hauteur}, "
                f"surface : {surface}")

    @staticmethod
    def plusGrand(r1, r2):
        s1 = r1._Rectangle__largeur * r1._Rectangle__hauteur
        s2 = r2._Rectangle__largeur * r2._Rectangle__hauteur
        return r1 if s1 >= s2 else r2


r1 = Rectangle(2, 3)
r2 = Rectangle(5, 4)
r3 = Rectangle(1, 7)

try:
    print(r1.__largeur)
except AttributeError as e:
    print(f"Accès refusé : {e}")

print(f"\nNombre de rectangles créés : {Rectangle.getNrect()}")
print(f"Plus grande surface : {Rectangle.getMaxSurface()}")

print(f"\n{r1}")
r1_copie = eval(repr(r1))
print(f"Copie via eval(repr) : {r1_copie}")

print(f"\nPlus grand (r1 vs r2) : {Rectangle.plusGrand(r1, r2)}")
print(f"Plus grand (r2 vs r3) : {Rectangle.plusGrand(r2, r3)}")