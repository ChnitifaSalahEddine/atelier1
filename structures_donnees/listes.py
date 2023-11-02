# 9. Initialisation et affichage de la liste
liste_langages = ['Python', 'Java', 'PHP', 'C', 'C++', 'Français', 'SQL', 'Arabe', 'PLSQL']
print("Liste des langages :")
for langage in liste_langages:
    print(langage)

# 10. Nombre d'éléments dans la liste
nombre_elements = len(liste_langages)
print(f"Le nombre d'éléments dans la liste est : {nombre_elements}")

# 11. Affichage de la liste de manière inversée
print("Liste inversée :")
liste_langages_inverse = list(reversed(liste_langages))
for langage in liste_langages_inverse:
    print(langage)

# 12. Affichage de la liste de manière triée
print("Liste triée :")
liste_langages_triee = sorted(liste_langages)
for langage in liste_langages_triee:
    print(langage)

# 13. Ajout du langage Assembleur dans la liste
liste_langages.append('Assembleur')
print("Liste après l'ajout d'Assembleur :", liste_langages)

# 14. Suppression des langages sans relation avec la programmation
liste_langages = [langage for langage in liste_langages if langage not in ['Français', 'Arabe']]
print("Liste après la suppression des langages non liés à la programmation :", liste_langages)

# 15. Nombre d'éléments dans la liste après la suppression
nombre_elements_apres_suppression = len(liste_langages)
print(f"Le nombre d'éléments dans la liste après la suppression est : {nombre_elements_apres_suppression}")

# 16. Nombre de caractères de chaque élément de la liste
print("Nombre de caractères de chaque élément de la liste :")
for langage in liste_langages:
    print(f"{langage} : {len(langage)}")

# 17. Vidage de la liste
liste_langages.clear()
print("Liste après vidage :", liste_langages)

# result :
# Liste des langages :
# Python
# Java
# PHP
# C
# C++
# Français
# SQL
# Arabe
# PLSQL
# Le nombre d'éléments dans la liste est : 9
# Liste inversée :
# PLSQL
# Arabe
# SQL
# Français
# C++
# C
# PHP
# Java
# Python
# Liste triée :
# Arabe
# C
# C++
# Français
# Java
# PHP
# PLSQL
# Python
# SQL
# Liste après l'ajout d'Assembleur : ['Python', 'Java', 'PHP', 'C', 'C++', 'Français', 'SQL', 'Arabe', 'PLSQL', 'Assembleur']
# Liste après la suppression des langages non liés à la programmation : ['Python', 'Java', 'PHP', 'C', 'C++', 'SQL', 'PLSQL', 'Assembleur']
# Le nombre d'éléments dans la liste après la suppression est : 8
# Nombre de caractères de chaque élément de la liste :
# Python : 6
# Java : 4
# PHP : 3
# C : 1
# C++ : 3
# SQL : 3
# PLSQL : 5
# Assembleur : 10
# Liste après vidage : []
#
# Process finished with exit code 0