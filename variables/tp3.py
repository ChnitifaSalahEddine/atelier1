import math

# Saisie du rayon et de la hauteur
rayon = float(input("Entrez la valeur du rayon : "))
hauteur = float(input("Entrez la valeur de la hauteur : "))

# Calcul du volume du cône
volume = (1/3) * math.pi * rayon**2 * hauteur

# Affichage du volume
print(f"Le volume du cône avec un rayon de {rayon} et une hauteur de {hauteur} est {volume}")
