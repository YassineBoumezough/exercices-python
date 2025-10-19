class Employe:
    def __init__(self, identifiant, nom, prenom,
                 jN, mN, aN,          # date de naissance (JJ, MM, AAAA)
                 jE, mE, aE,          # date d'embauche (JJ, MM, AAAA)
                 salaire):
        self.identifiant = identifiant
        self.nom = nom
        self.prenom = prenom

        # Naissance
        self.jN = int(jN); self.mN = int(mN); self.aN = int(aN)
        # Embauche
        self.jE = int(jE); self.mE = int(mE); self.aE = int(aE)

        self.salaire = float(salaire)

    def Age(self, jAuj, mAuj, aAuj):
        a = int(aAuj) - self.aN

        if (int(mAuj), int(jAuj)) < (self.mN, self.jN):
            a -= 1
        return a


    def Anciennete(self, jAuj, mAuj, aAuj):
        a = int(aAuj) - self.aE

        if (int(mAuj), int(jAuj)) < (self.mE, self.jE):
            a -= 1
        # jamais négatif
        if a < 0:
            a = 0
        return a
