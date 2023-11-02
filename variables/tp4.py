import math

# -4- Une machine découpe dans une plaque, des disques circulaires de rayon
#     rExt, percés d’un trou circulaire de rayon rInt avec rInt < rExt et ne
#     débordant pas du disque.

# a) Saisie des données
# Les données nécessaires sont le rayon extérieur (rExt)
# et le rayon intérieur (rInt) du disque. Vous devez vous
# assurer que rInt est inférieur à rExt.
rExt = float(input("Entrez le rayon extérieur du disque : "))
rInt = float(input("Entrez le rayon intérieur du trou circulaire : "))

# b) Calcul de la surface du disque découpé
# La formule pour calculer la surface d'un disque découpé est la différence entre
# les aires des deux cercles (le cercle extérieur moins le cercle intérieur).
# La formule est la suivante :

surface = math.pi * (rExt ** 2 - rInt ** 2)

# c) Affichage du résultat
print(f"La surface du disque découpé est : {surface}")

# result :

# Entrez le rayon extérieur du disque : 12
# Entrez le rayon intérieur du trou circulaire : 6
# La surface du disque découpé est : 339.29200658769764
#
# Process finished with exit code 0
