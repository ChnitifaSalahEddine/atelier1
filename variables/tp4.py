import math

# a) Saisie des données
#Les données nécessaires sont le rayon extérieur (rExt)
# et le rayon intérieur (rInt) du disque. Vous devez vous
# assurer que rInt est inférieur à rExt.
rExt = float(input("Entrez le rayon extérieur du disque : "))
rInt = float(input("Entrez le rayon intérieur du trou circulaire : "))

# b) Calcul de la surface du disque découpé
#La formule pour calculer la surface d'un disque découpé est la différence entre
# les aires des deux cercles (le cercle extérieur moins le cercle intérieur).
# La formule est la suivante :

surface = math.pi * (rExt**2 - rInt**2)

# c) Affichage du résultat
print(f"La surface du disque découpé est : {surface}")