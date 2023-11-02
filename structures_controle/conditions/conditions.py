# a. Saisie de 2 valeurs numériques et affichage de la plus petite
valeur_1 = float(input("Entrez la première valeur numérique : "))
valeur_2 = float(input("Entrez la deuxième valeur numérique : "))

if valeur_1 < valeur_2:
    print(f"La plus petite valeur est : {valeur_1}")
else:
    print(f"La plus petite valeur est : {valeur_2}")

# b. Affichage de la plus grande des 2 valeurs
if valeur_1 > valeur_2:
    print(f"La plus grande valeur est : {valeur_1}")
else:
    print(f"La plus grande valeur est : {valeur_2}")

# c. Vérification si les deux valeurs sont égales
if valeur_1 == valeur_2:
    print("Les deux valeurs sont égales.")
else:
    print("Les deux valeurs ne sont pas égales.")

# result :
# Entrez la première valeur numérique : 12
# Entrez la deuxième valeur numérique : 7
# La plus petite valeur est : 7.0
# La plus grande valeur est : 12.0
# Les deux valeurs ne sont pas égales.
#
# Process finished with exit code 0