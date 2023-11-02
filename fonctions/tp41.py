# Fonction pour afficher la table de multiplication jusqu'à 10 pour une variable donnée

def est_numerique(valeur):
    try:
        float(valeur)
        return True
    except ValueError:
        return False
def table_multiplication(variable):
    if est_numerique(variable):
        variable = float(variable)
        for i in range(11):
            resultat = variable * i
            print(f"{variable} * {i} = {resultat}")
    else:
        print("La variable n'est pas numérique.")

# Demander à l'utilisateur de saisir une variable numérique
variable = input("Entrez une variable numérique : ")

# Utiliser la fonction table_multiplication pour afficher la table de multiplication
table_multiplication(variable)

# result :

# Entrez une variable numérique : 36
# 36.0 * 0 = 0.0
# 36.0 * 1 = 36.0
# 36.0 * 2 = 72.0
# 36.0 * 3 = 108.0
# 36.0 * 4 = 144.0
# 36.0 * 5 = 180.0
# 36.0 * 6 = 216.0
# 36.0 * 7 = 252.0
# 36.0 * 8 = 288.0
# 36.0 * 9 = 324.0
# 36.0 * 10 = 360.0
#
# Process finished with exit code 0