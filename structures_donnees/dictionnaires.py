# 24. Initialisation et affichage du dictionnaire
mon_dictionnaire = {
    "nom": "Chnitifa",
    "prenom": "Salaheddine",
    "age": 28,
    "specialite": "Mobile engineer"
}
print("Dictionnaire d'informations personnelles :", mon_dictionnaire)

# 25. Parcours des valeurs du dictionnaire
print("Parcours des valeurs du dictionnaire :")
for valeur in mon_dictionnaire.values():
    print(valeur)

# 26. Parcours des clés du dictionnaire
print("Parcours des clés du dictionnaire :")
for cle in mon_dictionnaire.keys():
    print(cle)

# 27. Modification de la valeur d'âge
mon_dictionnaire["age"] -= 2
print("Dictionnaire après modification de l'âge :", mon_dictionnaire)

# 28. Ajout de la date d'obtention du Bac
mon_dictionnaire["date_obtention_bac"] = "20/06/2013"
print("Dictionnaire après ajout de la date d'obtention du Bac :", mon_dictionnaire)

# 29. Suppression de l'élément 'specialite'
if "specialite" in mon_dictionnaire:
    del mon_dictionnaire["specialite"]
print("Dictionnaire après suppression de 'specialite' :", mon_dictionnaire)

# 30. Vidage du dictionnaire
mon_dictionnaire.clear()
print("Le dictionnaire a été vidé :", mon_dictionnaire)

# result :
# Dictionnaire d'informations personnelles : {'nom': 'Chnitifa', 'prenom': 'Salaheddine', 'age': 28, 'specialite': 'Mobile engineer'}
# Parcours des valeurs du dictionnaire :
# Chnitifa
# Salaheddine
# 28
# Mobile engineer
# Parcours des clés du dictionnaire :
# nom
# prenom
# age
# specialite
# Dictionnaire après modification de l'âge : {'nom': 'Chnitifa', 'prenom': 'Salaheddine', 'age': 26, 'specialite': 'Mobile engineer'}
# Dictionnaire après ajout de la date d'obtention du Bac : {'nom': 'Chnitifa', 'prenom': 'Salaheddine', 'age': 26, 'specialite': 'Mobile engineer', 'date_obtention_bac': '20/06/2013'}
# Dictionnaire après suppression de 'specialite' : {'nom': 'Chnitifa', 'prenom': 'Salaheddine', 'age': 26, 'date_obtention_bac': '20/06/2013'}
# Le dictionnaire a été vidé : {}
#
# Process finished with exit code 0
