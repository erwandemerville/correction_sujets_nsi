# ===> EXERCICE 1 <===

# METHODE 1
def maxi(tab):
    ''' Fonction qui retourne un couple comportant la valeur maximale
    d'une liste d'entiers NATURELS et l'indice associé à cette valeur.
    :param tab: (list) Une liste d'entiers.
    :return: (tuple) Une couple (tuple) de deux éléments '''
    
    maximum = -1  # Variable qui contiendra la valeur max de la liste tab, initialisée à -1
    position = -1  # Variable qui contiendra l'indice de la valeur max de la liste tab, initialisée à -1
    for i in range(len(tab)):  # On parcourt le tableau tab, i allant de 0 à la taille de tab - 1
        if tab[i] > maximum:  # Si l'élément courant (en position i) est plus grand que maximum
            maximum = tab[i]  # On remplace l'ancien maximum par la valeur courante
            position = i  # On remplace l'ancienne position par la position courante i
    return (maximum, position)  # On retourne un couple contenant le max de tab et sa position

# METHODE 2 (en une seule ligne)
def maxi2(tab):
    return (max(tab), tab.index(max(tab)))
    # La fonction max de Python retourne le maximum d'une liste
    # La méthode index retourne l'indice de l'élément spécifié en argument

# ===> EXERCICE 2 <===

def positif(T):
    T2 = list(T)  # On fait une copie de la pile T dans T2
    T3 = []  # On crée une nouvelle pile vide dans T3
    while T2 != []:  # Tant que la liste T2 n'est pas vide
        x = T2.pop()  # On prend l'élément au sommet de la pile T2
        if x >= 0:  # Si l'élément dans x est positif
            T3.append(x)  # On ajoute l'élément x à la pile T3
    T2 = []  # T2 devient à présent une pile vide
    while T3 != []:  # Tant que la pile T3 n'est pas vide
        x = T3.pop()  # On prend l'élément au sommet de la pile T3
        T2.append(x)  # Puis on met cet élément x dans la pile T2
    print('T = ',T)  # On affiche (avec print) la pile de départ T
    return T2  # Puis on retourne la pile des éléments positifs T2

