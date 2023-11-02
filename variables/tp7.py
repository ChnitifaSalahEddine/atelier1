# -7- Écrire un programme qui réalise la saisie d’un nombre entier puis affiche la
# valeur ainsi saisie et son type. Essayer de dépasser la taille maximale des
# entiers. Expliquer.

# Saisie d'un nombre entier
entier_saisi = int(input("Entrez un nombre entier : "))

# Affichage de la valeur saisie et de son type
print("La valeur saisie est :", entier_saisi)
print("Le type de la valeur saisie est :", type(entier_saisi))

# Saisie d'un nombre entier très grand
print("Essayer de dépasser la taille maximale des entiers")
entier_tres_grand = 2 ** 1000

# Affichage de la valeur saisie et de son type
print("La valeur saisie est :", entier_tres_grand)
print("Le type de la valeur saisie est :", type(entier_tres_grand))

# result :
# Entrez un nombre entier : 1000000000000000000000000
# La valeur saisie est : 1000000000000000000000000
# Le type de la valeur saisie est : <class 'int'>
# Essayer de dépasser la taille maximale des entiers
# La valeur saisie est : 10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
# Le type de la valeur saisie est : <class 'int'>
#
# Process finished with exit code 0

# Expliquer :
# Python gère automatiquement les entiers de taille arbitrairement grande en utilisant des techniques
# telles que l'allocation dynamique de mémoire, ce qui signifie qu'il n'y a pas de limitations
# de taille pour les entiers en Python.
