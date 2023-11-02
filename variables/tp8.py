# -8- Ecrire un programme qui transforme un nombre de base décimale vers la
#     base binaire, et puis renvoyer son adresse mémoire.

# Saisie du nombre en base décimale
nombre_decimal = int(input("Entrez un nombre en base décimale : "))

# Conversion en binaire
nombre_binaire = bin(nombre_decimal)

# Adresse mémoire
adresse_memoire = id(nombre_binaire)

# Affichage du résultat
print(f"Le nombre en base binaire est : {nombre_binaire}")
print(f"L'adresse mémoire du nombre en base binaire est : {adresse_memoire}")

# result :
# Entrez un nombre en base décimale : 10
# Le nombre en base binaire est : 0b1010
# L'adresse mémoire du nombre en base binaire est : 4366862256
#
# Process finished with exit code 0