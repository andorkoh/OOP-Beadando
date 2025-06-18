from datetime import date

class Berles:
    def __init__(self, auto, datum):
        self.auto = auto
        self.datum = datum

    def __str__(self):
        return f"{self.auto.tipus} ({self.auto.rendszam}) - {self.auto.berleti_dij} Ft - {self.datum}"

    def uj_berles(auto, egyenleg, datum):
        if egyenleg < auto.berleti_dij:
            raise ValueError("Nincs elegendő pénz a bérléshez!")
        return Berles(auto, datum), auto.berleti_dij

    def lemondas(self):
        return self.auto.berleti_dij