# Demander à l'utilisateur de saisir un nombre
nombre = float(input("Entrez un nombre : "))

# Vérifier si le nombre est positif ou négatif
if nombre > 0:
    print("Le nombre est positif.")
elif nombre < 0:
    print("Le nombre est négatif.")
else:
    print("Le nombre est zéro.")

# Afficher le carré du nombre
print("Le carré de", nombre, "est", nombre ** 2)