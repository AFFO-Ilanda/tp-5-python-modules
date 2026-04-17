from maths.operations import addition, soustraction, multiplication
from maths.statistiques import moyenne, maximum, minimum
from utils.string_utils import inverser_chaine, compter_mots
import requests

print("Addition 5 + 3 =", addition(5, 3))
print("Soustraction 10 - 4 =", soustraction(10, 4))
print("Multiplication 7 * 2 =", multiplication(7, 2))

liste = [10, 20, 30, 40, 50]
print("Moyenne =", moyenne(liste))
print("Maximum =", maximum(liste))
print("Minimum =", minimum(liste))

texte = "Bonjour tout le monde"
print("Chaîne inversée :", inverser_chaine(texte))
print("Nombre de mots :", compter_mots(texte))

def tester_requete(url: str):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print("Requête réussie !")
            print(response.text[:300])
        else:
            print(f"Erreur HTTP : {response.status_code}")
    except Exception as e:
        print(f"Erreur de connexion : {e}")

tester_requete("https://www.example.com")
