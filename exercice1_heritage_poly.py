class CapteurMeteo:
    def __init__(self, nom, emplacement, date_installation):
        self.nom = nom
        self.emplacement = emplacement
        self.date_installation = date_installation

    def afficher_infos(self):
        print(f"Nom: {self.nom}\nEmplacement: {self.emplacement}\nDate d'installation: {self.date_installation}")


class CapteurTemperature(CapteurMeteo):
    def __init__(self, nom, emplacement, date_installation, plage_mesure):
        super().__init__(nom, emplacement, date_installation)
        self.plage_mesure = plage_mesure

    def afficher_infos(self):
        super().afficher_infos()
        print(f"Type: Capteur de Température\nPlage de mesure: {self.plage_mesure}")


class CapteurHumidite(CapteurMeteo):
    def __init__(self, nom, emplacement, date_installation, plage_mesure):
        super().__init__(nom, emplacement, date_installation)
        self.plage_mesure = plage_mesure

    def afficher_infos(self):
        super().afficher_infos()
        print(f"Type: Capteur d'Humidité\nPlage de mesure: {self.plage_mesure}")


# Création d'instances
capteur_meteo = CapteurMeteo("Capteur Météo 1", "Extérieur", "2023-01-01")
capteur_temperature = CapteurTemperature("Capteur Température 1", "Intérieur", "2023-02-15", "-10°C à 40°C")
capteur_humidite = CapteurHumidite("Capteur Humidité 1", "Salle de bain", "2023-03-10", "0% à 100%")

# Affichage des informations
print("Informations du Capteur Météo :")
capteur_meteo.afficher_infos()
print("\nInformations du Capteur de Température :")
capteur_temperature.afficher_infos()
print("\nInformations du Capteur d'Humidité :")
capteur_humidite.afficher_infos()
