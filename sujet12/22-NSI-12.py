# ===> EXERCICE 1 <===

def moyenne(tab):
    if tab:  # Si le tableau tab n'est pas vide
        somme = sum(tab)  # Variable qui contient la somme des éléments de tab
        nombre = len(tab)  # Variable contenant le nombre d'éléments dans tab
        return somme / nombre  # On renvoie la moyenne
    else:  # Si le tableau tab est vide
        print('erreur')  # On affiche 'erreur'
        
# Méthode 2 (sans utiliser la fonction 'sum')
def moyenne2(tab):
    if tab:  # Si le tableau tab n'est pas vide
        somme = 0  # Variable qui contiendra la somme des éléments de tab
        nombre = len(tab)  # Variable contenant le nombre d'éléments dans tab
        for el in tab:  # On parcourt les éléments de tab
            somme += el  # On ajoute l'élément el à somme
        return somme / nombre  # On renvoie la moyenne
    else:  # Si le tableau tab est vide
        print('erreur')  # On affiche 'erreur'


# ===> EXERCICE 2 <===

def tri(tab):
    #i est le premier indice de la zone non triee, j le dernier indice. 
    #Au debut, la zone non triee est le tableau entier.
    i = 0  # L'indice de début de la zone non triée est initialement 0
    j = len(tab) - 1  # L'indice de fin de la zone non triée est initialement le dernier indice du tableau tab
    while i != j :  # Tant que l'indice du début de la zone non triée est différent de l'indice de fin
        if tab[i] == 0:  # Si l'élément d'indice i vaut 0
            i = i + 1  # L'élément d'indice i ne fait plus partie de la zone non triée (il est dans la zone de 0)
        else :  # Si l'élément d'indice i vaut 1, on l'échange l'élément i avec l'élément j
            valeur = tab[j]  # On met de côté l'élément d'indice j (dans une variable valeur)
            tab[j] = tab[i]  # On copie l'élément d'indice i à la position j
            tab[i] = valeur  # On met l'élément mis de côté (dans valeur) à la position i pour terminer la permutation
            j = j - 1  # L'indice de fin de la zone non triée diminue de 1
    return tab  # On renvoie le tableau ainsi modifié
