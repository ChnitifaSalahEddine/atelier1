# Fonction pour vérifier si une chaîne est numérique
def est_numerique(valeur):
    try:
        float(valeur)
        return True
    except ValueError:
        return False

# Demander à l'utilisateur de saisir deux valeurs numériques
valeur1 = input("Entrez la première valeur numérique : ")
valeur2 = input("Entrez la deuxième valeur numérique : ")

# Vérifier si les valeurs saisies sont numériques
if est_numerique(valeur1) and est_numerique(valeur2):
    print("Les deux valeurs saisies sont numériques.")
else:
    print("Au moins l'une des valeurs saisies n'est pas numérique.")

# Fonction pour calculer et afficher la somme
def somme(valeur1, valeur2):
    if est_numerique(valeur1) and est_numerique(valeur2):
        somme = float(valeur1) + float(valeur2)
        print(f"La somme des deux valeurs est : {somme}")
    else:
        print("Au moins l'une des valeurs saisies n'est pas numérique.")


# Utiliser la fonction somme pour calculer et afficher la somme
somme(valeur1, valeur2)

# Fonction pour calculer et retourner la multiplication
def multiplication(valeur1, valeur2):
    if est_numerique(valeur1) and est_numerique(valeur2):
        produit = float(valeur1) * float(valeur2)
        return produit
    else:
        return None

# Utiliser la fonction multiplication pour calculer le produit
resultat_multiplication = multiplication(valeur1, valeur2)

if resultat_multiplication is not None:
    print(f"Le produit des deux valeurs est : {resultat_multiplication}")
else:
    print("Au moins l'une des valeurs saisies n'est pas numérique.")


# Fonction pour calculer et retourner la division
def division(valeur1, valeur2):
    if est_numerique(valeur1) and est_numerique(valeur2):
        if float(valeur2) != 0:
            resultat_division = float(valeur1) / float(valeur2)
            return resultat_division
        else:
            return None
    else:
        return None


# Utiliser la fonction division pour calculer la division
resultat_division = division(valeur1, valeur2)

if resultat_division is not None:
    print(f"Le résultat de la division des deux valeurs est : {resultat_division}")
else:
    print("Division par zéro ou au moins l'une des valeurs saisies n'est pas numérique.")


