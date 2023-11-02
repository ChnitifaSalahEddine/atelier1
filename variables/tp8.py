# Saisie du nombre en base décimale
nombre_decimal = int(input("Entrez un nombre en base décimale : "))

# Conversion en binaire
nombre_binaire = bin(nombre_decimal)

# Adresse mémoire
adresse_memoire = id(nombre_binaire)

# Affichage du résultat
print(f"Le nombre en base binaire est : {nombre_binaire}")
print(f"L'adresse mémoire du nombre en base binaire est : {adresse_memoire}")