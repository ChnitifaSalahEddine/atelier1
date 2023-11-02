# Saisie de 2 chaînes de caractères
chaine_1 = input("Entrez la première chaîne de caractères : ")
chaine_2 = input("Entrez la deuxième chaîne de caractères : ")

# Affichage de la plus grande et de la plus petite chaîne
if len(chaine_1) > len(chaine_2):
    print(f"La chaîne '{chaine_1}' est plus grande que la chaîne '{chaine_2}'.")
    print(f"La chaîne '{chaine_2}' est plus petite que la chaîne '{chaine_1}'.")
elif len(chaine_1) < len(chaine_2):
    print(f"La chaîne '{chaine_2}' est plus grande que la chaîne '{chaine_1}'.")
    print(f"La chaîne '{chaine_1}' est plus petite que la chaîne '{chaine_2}'.")
else:
    print(f"Les deux chaînes ont la même longueur.")


# result :
# Entrez la première chaîne de caractères : salaheddine
# Entrez la deuxième chaîne de caractères : chnitifa
# La chaîne 'salaheddine' est plus grande que la chaîne 'chnitifa'.
# La chaîne 'chnitifa' est plus petite que la chaîne 'salaheddine'.
#
# Process finished with exit code 0