# -6- Écrire un programme, qui ajoute une chaîne de caractères à un nombre entier
# (Exemple la chaîne ”le chat” et le nombre 3 pour donner le chat 3), et puis
# renvoyer la taille de chaine.

# Définition de la chaîne de caractères et du nombre entier
chaine = "le chat"
nombre = 3

# Ajout de la chaîne de caractères au nombre entier
chaine_result = chaine + " " + str(nombre)

# Renvoyer la taille de la chaîne résultante
taille_chaine_result = len(chaine_result)

# Afficher la chaîne résultante et sa taille
print("La chaîne résultante est :", chaine_result)
print("La taille de la chaîne résultante est :", taille_chaine_result)

# result :

# La chaîne résultante est : le chat 3
# La taille de la chaîne résultante est : 9
#
# Process finished with exit code 0
