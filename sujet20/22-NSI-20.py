# ===> EXERCICE 1 <===

def xor(t1, t2):
    ''' Renvoie un tableau contenant les bits qui résultent de l'opération
    xor effectuée entre chaque bit de t1 et chaque bit de même indice de t2.
    :param t1: (list) Une liste de bits
    :param t2: (list) Une autre liste de bits
    :return: (list) La liste qui résulte de l'opération
    :CU: Les deux listes sont de même taille '''
    
    tab = []  # On crée un tableau vide qui contiendra les bits à la fin des opérations entre t1 et t2
    for i in range(len(t1)) :  # i va de 0 jusqu'à l'indice du dernier élément de t1
        if t1[i] == t2[i]:  # Si les deux bits de même indice de t1 et t2 correspondent
            tab.append(0)  # On ajoute 0 à tab
        else:
            tab.append(1)  # Sinon on ajoute 1 à tab
    return tab  # Enfin, on renvoie le tableau final

# ===> EXERCICE 2 <===

class Carre:
    def __init__(self, tableau = [[]]):
        self.ordre = len(tableau)
        self.valeurs = tableau
    
    def affiche(self):
        '''Affiche un carré'''
        for i in range(self.ordre):
            print(self.valeurs[i])
    
    def somme_ligne(self, i):
        '''Calcule la somme des valeurs de la ligne i'''
        return sum(self.valeurs[i])
    
    def somme_col(self, j):
        '''calcule la somme des valeurs de la colonne j'''
        return sum([self.valeurs[i][j] for i in range(self.ordre)])

def est_magique(carre):
    n = carre.ordre  # n contient l'ordre du carré
    s = carre.somme_ligne(0)  # s contient la somme des éléments de la première ligne, valeur utilisée comme référence
        
    #test de la somme de chaque ligne
    for i in range(1, n):  # On parcourt chaque ligne du carré, sauf la première qui a déjà été sommée
        if carre.somme_ligne(i) != s:  # Si la somme des éléments d'une ligne n'est pas de valeur s
            return False  # Le carré n'est pas magique, on renvoie False
        
    #test de la somme de chaque colonne
    for j in range(n):  # On parcourt chaque colonne du carré
        if carre.somme_col(i) != s:  # Si la somme des éléments d'une colonne n'est pas de valeur s
            return False  # Le carré n'est pas magique, on renvoie False
         
    #test de la somme de chaque diagonale
    if sum([carre.valeurs[k][k] for k in range(n)]) != s:  # La première diagonale est la liste des éléments d'indices k, k
            return False  # Le carré n'est pas magique, on renvoie False
    if sum([carre.valeurs[k][n-1-k] for k in range(n)]) != s:  # La deuxième diagonale est la liste des éléments d'indices k, n-1-k
            return False  # Le carré n'est pas magique, on renvoie False
    
    return s  # Si on est arrivé au bout, le carré est magique et on renvoie la valeur de la somme


