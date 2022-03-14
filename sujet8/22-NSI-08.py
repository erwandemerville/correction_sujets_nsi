# ===> EXERCICE 1 <===

def recherche(elt, tab):
    ''' Renvoie la première occurence de elt dans tab s'il elt est trouvé,
    renvoie -1 si elt n'est pas trouvé.
    :param elt: (int) Un nombre entier à chercher
    :param tab: (list) Le tableau dans lequel cherche l'élément elt
    :return: (int) La position de l'élément cherché, ou -1 '''
    
    for i in range(len(tab)):  # On parcourt les éléments de tab, i allant de 0 à taille de tab - 1
        if tab[i] == elt:  # Si l'élément courant du tableau est égal à l'élément recherché
            return i  # On renvoie la position i de l'élément
    return -1  # On renvoie -1 si l'élément n'a pas été trouvé

# Autre méthode (avec la méthode index) :
def recherche2(elt, tab):
    for el in tab:  # On parcourt les éléments de tab
        if el == elt:  # Si l'élément courant du tableau est égal à l'élément recherché
            return tab.index(el)  # On renvoie la position de l'élément récupérée avec la méthode index
    return -1  # On renvoie -1 si l'élément n'a pas été trouvé
        

# ===> EXERCICE 2 <===

def insere(a, tab):
    ''' Le fonctionnement de cet algorithme est le suivant :
    - On place l'élément a à la fin de la liste tab
    - Puis on permute les éléments deux par deux en partant de la fin
    - On s'arrête lorsque a se trouve à la bonne position '''
    
    l = list(tab) # l contient les mêmes éléments que tab
    l.append(a)  # Ajouter l'élément a à la liste l
    i = len(l) - 2  # Contient l'indice de l, initialisé à taille de l - 2, utilisé dans le while qui suit
    while a < l[i] and i >= 0:  # Tant que a est inférieur à l'élément courant et qu'on a pas fini de parcourir tab
      l[i+1] = l[i]  # On permute l'élément i avec a : l'élément d'indice i est mis à la position i + 1...
      l[i] = a  # ...et a est mis à la position i
      i = i - 1  # Décrémenter i
    return l  # On renvoie la liste contenant l'élément a ajouté
