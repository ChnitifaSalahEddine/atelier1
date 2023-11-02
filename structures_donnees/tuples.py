# 18. Initialisation et affichage du tuple
tuple_bio = ('ADN', 'ARN', 'Protéine', 'Virus', 'Bactérie')
print("Tuple d'éléments biochimiques :", tuple_bio)

# 19. Nombre d'éléments du tuple
nombre_elements_tuple = len(tuple_bio)
print(f"Le nombre d'éléments dans le tuple est : {nombre_elements_tuple}")

# 20. Vérification de la présence de 'Corona' dans le tuple
corona_present = 'Corona' in tuple_bio
print(f"Corona est{' ' if corona_present else ' pas '}présent dans le tuple.")

# 21. Position de l'élément 'Protéine'
position_proteine = tuple_bio.index('Protéine')
print(f"La position de 'Protéine' dans le tuple est : {position_proteine}")

# 22. Nombre de caractères de chaque élément du tuple
print("Nombre de caractères de chaque élément du tuple :")
for element in tuple_bio:
    print(f"{element} : {len(element)}")

# 23. Suppression complète du tuple
del tuple_bio
print("Le tuple a été complètement supprimé.")

# result :
# Tuple d'éléments biochimiques : ('ADN', 'ARN', 'Protéine', 'Virus', 'Bactérie')
# Le nombre d'éléments dans le tuple est : 5
# Corona est pas présent dans le tuple.
# La position de 'Protéine' dans le tuple est : 2
# Nombre de caractères de chaque élément du tuple :
# ADN : 3
# ARN : 3
# Protéine : 8
# Virus : 5
# Bactérie : 8
# Le tuple a été complètement supprimé.
#
# Process finished with exit code 0