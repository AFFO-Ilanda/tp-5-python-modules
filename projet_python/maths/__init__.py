from .operations import addition, soustraction, multiplication
from .statistiques import moyenne, maximum, minimum, somme_des_carres

__all__ = ["addition", "soustraction", "multiplication",
           "moyenne", "maximum", "minimum"]

# Remarque : somme_des_carres n'est PAS dans __all__ (volontaire)
