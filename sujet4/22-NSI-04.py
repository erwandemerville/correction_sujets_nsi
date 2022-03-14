# ===> EXERCICE 1 <===

def recherche(tableau):
    ''' Renvoie une liste des couples d'entiers consécutifs successifs de tableau.
    :param tableau: (list) Une liste d'entiers
    :return: (list) Une nouvelle liste de couples (tuples) d'entiers '''
    
    lst = []  # Variable qui contiendra la liste finale, initialisée à une liste vide
    for i in range(len(tableau) - 1):  # On parcourt le tableau en s'arrêtant à l'avant-dernier élément
        if tableau[i+1] == tableau[i] + 1:  # Si l'élément suivant dans le tableau est égal à l'élément courant + 1
            lst.append((tableau[i], tableau[i+1]))  # On ajoute à lst un couple contenant les deux éléments
    return lst  # Enfin, on renvoie lst

# ===> EXERCICE 2 <===

def propager(M, i, j, val):
    ''' Modifie le tableau à deux dimensions M en mettant à la valeur val tous les
    pixels de la composante du pixel d'indices i et j.
    :param M: (list of list) Tableau à 2 dimensions
    :param i: (int) Le numéro de la ligne (la première ligne correspond à l'indice 0)
    :param j: (int) Le numéro de la colonne (la première colonne correspond à l'indice 0)
    :param val: (int) Valeur à laquelle mettre les pixels de la composante '''
    
    if M[i][j] == 0:  # Si l'élément de M d'indices i (ligne) et j (colonne) vaut 0
        return  # On ne renvoie rien, et la fonction s'arrête ici (un return met fin à la fonction)
    
    # Si l'élément ne vaut pas 0 (il vaut donc 1), on continue la fonction :
    M[i][j] = val  # L'élément d'indices i et j prend la valeur val

    # l'élément en haut fait partie de la composante
    if ((i-1) >= 0 and M[i-1][j] == 1):  # Si on est pas tout en haut du tableau ET que le pixel juste au dessus vaut 1
        propager(M, i-1, j, val)  # On rappelle la fonction propager sur le pixel du dessus

    # l'élément en bas fait partie de la composante
    if ((i+1) < len(M) and M[i+1][j] == 1):  # Si on est pas tout en bas du tableau ET que le pixel juste en dessous vaut 1
        propager(M, i+1, j, val)  # On rappelle la fonction propager sur le pixel du dessous

    # l'élément à gauche fait partie de la composante
    if ((j-1) >= 0 and M[i][j-1] == 1):  # Si on est pas tout à gauche du tableau ET que le pixel juste à gauche vaut 1
        propager(M, i, j-1, val)  # On rappelle la fonction propager sur le pixel de gauche

    # l'élément à droite fait partie de la composante
    if ((j+1) < len(M) and M[i][j+1] == 1): # Si on est pas tout à droite du tableau ET que le pixel juste à droite vaut 1
        propager(M, i, j+1, val)  # On rappelle la fonction propager sur le pixel de droite
