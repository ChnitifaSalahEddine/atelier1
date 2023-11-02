# Écrire un programme qui affiche le type du résultat des instructions
# suivantes:
# a=3
# a= =3

# Assignation d'une valeur à la variable a
a=3

# Assignation d'une valeur à la variable a avec un signe égal après le premier égal
# a= =3

# Affichage du type du résultat pour les deux instructions
print("Le type de la variable a est :", type(a))

# result :

#   File "/Users/salaheddine/PycharmProjects/atelier1/variables/tp5.py", line 10
#     a= =3
#        ^
# SyntaxError: invalid syntax
#
# Process finished with exit code 1

# Si vous essayez d'exécuter le code avec a= =3,
# vous obtiendrez une erreur de syntaxe indiquant que l'opérateur n'est pas reconnu.