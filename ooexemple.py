class Vehicule:
    nombre = 0
    nom_vehicule :str
    #####pour creer le constructeu en python
    def __init__(self, v_nom_vehicule, v_moteur, v_couleur, v_marque):
        self.nom_vehicule= v_nom_vehicule
        self.moteur = v_moteur
        self.couleur =v_couleur
        self.marque= v_marque
        self.number += 1


    def afficher(self):
        print(f"c'est le vehicule {self.nom_vehicule} {self.marque}")

        v1= Vehicule("prado", "diesel", "grise","toyota" )
        print(v1.afficher())

    