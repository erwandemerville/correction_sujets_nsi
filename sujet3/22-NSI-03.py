# ===> EXERCICE 1 <===

def delta(tableau):
    ''' Fonction qui renvoie un tableau contenant les valeurs compressées.
    :param tableau: (list) Liste des éléments à compresser
    :return (list): Une liste contenant les éléments compressés avec le delta encoding '''
    
    tab_final = [tableau[0]]  # Variable qui contiendra le tableau final, initialisé avec le premier élément
    for i in range(1, len(tableau)):  # On parcourt le tableau en commençant au deuxième élément
        tab_final.append(tableau[i] - tableau[i - 1])  # On ajoute la soustraction des deux éléments d'indices i et i - 1
    return tab_final  # On renvoie enfin le tableau final
    
# ===> EXERCICE 2 <===

class Noeud:
    def __init__(self, g, v, d):
        self.gauche = g
        self.valeur = v
        self.droit = d
    
    def __str__(self):
        return str(self.valeur)
    
    def est_une_feuille(self):
        '''Renvoie True si et seulement si le noeud est une feuille'''
        return self.gauche is None and self.droit is None


def expression_infixe(e):
    s = ''  # On crée une chaîne s initialement vide
    if e.gauche is not None:  # Si le sous-arbre gauche n'EST PAS vide
        s = '(' + s + expression_infixe(e.gauche)  # Ouvrir parenthèse et ajouter à la chaîne l'expression du ss-arbre gauche
    s = s + str(e)  # On ajoute la valeur du noeud à la chaîne
    if e.droit is not None:  # Si le sous-arbre droit n'EST PAS vide
        s = s + expression_infixe(e.droit) + ')'  # Ajouter l'expression du ss-arbre droit à la chaîne et fermer la parenthèse
    if s :  # Cette condition n'est pas nécessaire, on pourrait la retirer
        return s  # On renvoie la chaîne finale
    
# Remarque : La fonction précédente est un peu étrange, car dans une structure d'arbre arithmétique,
# un arbre ne peut pas ne contenir qu'un sous-arbre gauche ou qu'un sous-arbre droit.
# Soit il s'agit d'une feuille (contenant une valeur), soit il s'agit d'un arbre avec un sous-arbre gauche et droit.
# Il serait plus pertinent et plus simple d'écrire cette fonction comme suit :
#
# def expression_infixe(e):
#     if e.est_une_feuille():
#         return str(e)
#     else:
#         return '(' + expression_infixe(e.gauche) + str(e) + expression_infixe(e.droit) + ')'