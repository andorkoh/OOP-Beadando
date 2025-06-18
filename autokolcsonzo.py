class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def berelheto_autok(self):
        foglalt = {berles.auto.rendszam for berles in self.berlesek}
        return [auto for auto in self.autok if auto.rendszam not in foglalt]

    def lemondas(self, rendszam):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam:
                self.berlesek.remove(berles)
                return berles.auto