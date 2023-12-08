import re

# Liste de numéros de plaques d'immatriculation
license_plate_list = ["AB-123-CD", "12-BTS-67", "IL-89Z-01", "BT-321-SN"]

# Expression régulière
pattern = re.compile(r'^[A-Z]{2}-\d{3}-[A-Z]{2}$')

# Création d'une liste vide pour stocker les plaques valides
valid_license_plates = []

# Parcours de la liste des numéros de plaques
for plate in license_plate_list:
    # Vérification si la plaque correspond au motif
    if pattern.match(plate):
        # Ajout de la plaque à la liste des plaques valides
        valid_license_plates.append(plate)

# Affichage des numéros de plaques valides
print("Numéros de plaques valides :")
for valid_plate in valid_license_plates:
    print(valid_plate)