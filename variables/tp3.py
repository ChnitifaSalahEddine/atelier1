import math

# -3- Écrire un programme qui, à partir de la saisie d’un rayon et d’une hauteur,
#     calcule le volume d’un cône droit :

# Saisie du rayon et de la hauteur
rayon = float(input("Entrez la valeur du rayon : "))
hauteur = float(input("Entrez la valeur de la hauteur : "))

# Calcul du volume du cône
volume = (1/3) * math.pi * rayon**2 * hauteur

# Affichage du volume
print(f"Le volume du cône avec un rayon de {rayon} et une hauteur de {hauteur} est {volume}")

# result :

# Entrez la valeur du rayon : 4
# \Entrez la valeur de la hauteur : 12
# Le volume du cône avec un rayon de 4.0 et une hauteur de 12.0 est 201.06192982974676
#
# Process finished with exit code 0
