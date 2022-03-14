# ===> EXERCICE 1 <===

# Méthode 1
def nombre_de_mots(phrase):
    ''' Retourne le nombre de mots dans phrase.
    :param phrase: (str) Une phrase
    :return: (int) Le nombre de mots
    Note : Le nombre de mots dans une phrase correspond à la somme des espaces et éventuellement du point
    de fin de la phrase. '''
    
    nb_mots = 0  # On crée un compteur du nombre de mots, initialisé à 0
    for caractere in phrase:  # On parcourt chaque caractère de notre phrase
        if caractere == ' ' or caractere == '.':  # Si le caractère est un espace ou un point
            nb_mots += 1  # On incrémente le compteur de mots
    return nb_mots  # On retourne enfin le nombre de mots

# Méthode 2 (avec la méthode split)
def nombre_de_mots2(phrase):
    tab = phrase.split(' ')  # Créer un tableau des éléments de phrase séparés par un espace
    if phrase[-1] == '.':  # Si le dernier élément de la phrase est un point
        return len(tab)  # On renvoie la taille de tab
    else:  # Sinon
        return len(tab) - 1  # On renvoie la taille de tab - 1 (car le point d'exclamation/d'interrogation est aussi dans tab)
    
# ===> EXERCICE 2 <===

class Noeud:
    '''
    Classe implémentant un noeud d'arbre binaire 
    disposant de 3 attributs :
    - valeur : la valeur de l'étiquette,
    - gauche : le sous-arbre gauche.
    - droit : le sous-arbre droit.
    '''
    def __init__(self, v, g, d):
        self.valeur = v
        self.gauche = g
        self.droite = d
        
class ABR:
    '''
    Classe implémentant une structure 
    d'arbre binaire de recherche.
    '''
    
    def __init__(self):
        '''Crée un arbre binaire de recherche vide'''
        self.racine = None
        
    def est_vide(self):
        '''Renvoie True si l'ABR est vide et False sinon.'''
        return self.racine is None
    
    def parcours(self, tab = []):
        '''
        Renvoie la liste tab complétée avec tous les 
        éléments de 
        l'ABR triés par ordre croissant.
        Le parcours à effectuer est un parcours INFIXE (sous-arbre gauche, valeur, sous-arbre droit)
        '''
        if self.est_vide():  # Si l'arbre binaire de recherche est vide
            return tab  # On renvoie tab sans rien ajouter dedans
        else:  # Sinon
            self.racine.gauche.parcours(tab)  # On parcourt le sous-arbre binaire de recherche gauche (le résultat sera ajouté dans tab)
            tab.append(self.racine.valeur)  # On ajoute à tab la valeur du noeud racine
            self.racine.droite.parcours(tab)  # On parcourt le sous-arbre binaire de recherche droit (le résultat sera ajouté dans tab)
            return tab  # On renvoie tab
        
    def insere(self, element):
        '''Insère un élément dans l'arbre binaire de recherche.'''
        if self.est_vide():
            self.racine = Noeud(element, ABR(), ABR())
        else:
            if element < self.racine.valeur:
                self.racine.gauche.insere(element)
            else : 
                self.racine.droite.insere(element)
    
    def recherche(self, element):
        '''
        Renvoie True si element est présent dans l'arbre 
        binaire et False sinon.
        '''
        if self.est_vide():  # Si l'ABR est vide
            return False  # On renvoie False (car l'élément cherché n'est pas dedans)
        else:  # Sinon
            if element < self.racine.valeur:  # Si l'élément est avant la valeur du noeud racine
                return self.racine.gauche.recherche(element)  # On recherche element dans le sous-arbre gauche
            elif element > self.racine.valeur:  # Si l'élément est après la valeur du noeud racine
                return self.racine.droite.rercherche(element)  # On recherche element dans le sous-arbre droit
            else:
                return True  #  L'élément cherché est égal à la valeur du noeud racine, on renvoie True
