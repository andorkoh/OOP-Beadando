class Auto:
    def __init__(self, rendszam, tipus, berleti_dij):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berleti_dij = berleti_dij

    def __str__(self):
        return f"{self.tipus} ({self.rendszam}) - {self.berleti_dij} Ft/nap"