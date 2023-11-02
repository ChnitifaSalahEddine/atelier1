
# -35- Écrire un programme qui affiche un joli sapin de Noël, dont la taille est donnée
# par l’utilisateur. Exemple pour une taille de 12 lignes :
def afficher_sapin(taille):
    for i in range(1, taille + 1):
        espaces = " " * (taille - i)
        etoiles = "ˆ" * (2*i - 1)
        print(espaces + etoiles)

# Demander à l'utilisateur la taille du sapin
taille_sapin = int(input("Entrez la taille du sapin : "))
afficher_sapin(taille_sapin)

# result :

# Entrez la taille du sapin : 12
#            ˆ
#           ˆˆˆ
#          ˆˆˆˆˆ
#         ˆˆˆˆˆˆˆ
#        ˆˆˆˆˆˆˆˆˆ
#       ˆˆˆˆˆˆˆˆˆˆˆ
#      ˆˆˆˆˆˆˆˆˆˆˆˆˆ
#     ˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆ
#    ˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆ
#   ˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆ
#  ˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆ
# ˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆˆ
#
# Process finished with exit code 0

