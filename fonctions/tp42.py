
# Fonction pour afficher la table de multiplication de 0 à 10
# pour une variable donnée en utilisant lambda et map

# Fonction pour vérifier si une chaîne est numérique
def est_numerique(valeur):
    try:
        float(valeur)
        return True
    except ValueError:
        return False

def table_multiplication(variable):
    if est_numerique(variable):
        variable = float(variable)
        valeurs = range(11)
        resultats = map(lambda x: variable * x, valeurs)
        for i, resultat in enumerate(resultats):
            print(f"{variable} * {i} = {resultat}")
    else:
        print("La variable n'est pas numérique.")

# Demander à l'utilisateur de saisir une variable numérique
variable = input("Entrez une variable numérique : ")

# Utiliser la fonction table_multiplication pour afficher la table de multiplication
table_multiplication(variable)

# result :

# Entrez une variable numérique : 12
# 12.0 * 0 = 0.0
# 12.0 * 1 = 12.0
# 12.0 * 2 = 24.0
# 12.0 * 3 = 36.0
# 12.0 * 4 = 48.0
# 12.0 * 5 = 60.0
# 12.0 * 6 = 72.0
# 12.0 * 7 = 84.0
# 12.0 * 8 = 96.0
# 12.0 * 9 = 108.0
# 12.0 * 10 = 120.0
#
# Process finished with exit code 0