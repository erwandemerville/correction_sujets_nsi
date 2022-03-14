# ===> EXERCICE 1 <===

def rechercheMinMax(tab):
    ''' Fonction qui renvoie la plus petite et la plus grande valeur du tableau
    tab sous la forme d'un dictionnaire à deux clés 'min' et 'max'.
    :param tab: (list) Une liste (= tableau) de nombres non triés
    :return: (dict) Un dictionnaire comportant l'élément 'min' et l'élément 'max' '''
    
    minimum = None  # On crée une variable qui contiendra le minimum du tableau, initialisée à None
    maximum = None  # On crée une variable qui contiendra le maximum du tableau, initialisée à None
    for el in tab:  # On parcourt la liste tab
        if not minimum or el < minimum:  # Si minimum vaut None ou que l'élément courant el est plus petit
            minimum = el  # On remplace l'ancien minimum par cet élément
        if not maximum or el > maximum:  # Si maximum vaut None ou que l'élément courant el est plus grand
            maximum = el  # On remplace l'ancien maximum par cet élément
    return {'min': minimum, 'max': maximum}  # On renvoie enfin le dictionnaire final
    
# ===> EXERCICE 2 <===

class Carte:
    """Initialise Couleur (entre 1 a 4), et Valeur (entre 1 a 13)"""
    def __init__(self, c, v):
        assert 1 <= c <= 4, 'Couleur incorrecte'  # Assertion permettant de s'assurer que la couleur soit entre 1 et 4
        assert 1 <= v <= 13, 'Valeur incorrecte'  # Assertion permettant de s'assurer que la valeur soit entre 1 et 13
        self.Couleur = c
        self.Valeur = v

    """Renvoie le nom de la Carte As, 2, ... 10, Valet, Dame, Roi"""
    def getNom(self):
        if (self.Valeur > 1 and self.Valeur < 11):
            return str(self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"

    """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle)"""
    def getCouleur(self):
        return ['pique', 'coeur', 'carreau', 'trefle' ][self.Couleur - 1]

class PaquetDeCarte:
    def __init__(self):
        self.contenu = []

    """Remplit le paquet de cartes"""
    def remplir(self):
        # Boucle permettant de créer les 52 cartes (13 cartes de 4 couleurs différentes)
        self.contenu = [Carte(couleur, valeur) for couleur in range(1, 5) for valeur in range(1, 14)]

    """Renvoie la Carte qui se trouve a  la position donnee"""
    def getCarteAt(self, pos):
        # Assertion permettant de vérifier que self.contenu ne soit pas vide (que le paquet ait bien été rempli)
        assert self.contenu, 'Le paquet de carte est vide'
        
        if 0 <= pos < 52:  # On s'assure que l'indice pos soit bien entre 0 et 51 (c-à-d l'indice d'une carte)
            return self.contenu[pos]  # Si c'est le cas, on retourne la carte d'indice pos