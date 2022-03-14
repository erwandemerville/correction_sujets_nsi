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

def recherche(gene, seq_adn):
    n = len(seq_adn)  # n prend la valeur de la taille de la séquence ADN
    g = len(gene)  # g prend la valeur de la taille du gène
    i = 0  # L'indice i correspond à la position dans la séquence ADN (par défaut 0)
    trouve = False
    while i < n - g and trouve == False :  # Voir la note 1 en dessous
        j = 0  # L'indice j correspond à la position dans le gène, initialisée à 0
        while j < g and gene[j] == seq_adn[i+j]:  # Tant que l'élément de la séquence correspond à l'élément du gène
            j += 1  # On incrémente j
        if j == g:  # Si j a la valeur de la taille du gène (ce qui signifie qu'on a trouvé tout le gène)
            trouve = True  # On passe "trouve" à True (vrai)
        i += 1  # On incrémente i
    return trouve  # On retourne le booléen trouve (qui vaut True ou False)

# Note 1 : La boucle continue tant que l'on a pas trouvé tout le gène,
# et s'arrête à n - g car si on s'arrête à n (au bout de la séquence ADN),
# on peut avoir une erreur si par exemple on fait recherche("GCCD", "GTACAAATCTTGCC")
# car lors de la comparaison de l'ADN et du gène, on dépassera la taille de l'ADN.
