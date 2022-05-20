# ===> EXERCICE 1 <===

def multiplication(n1, n2):
    produit = 0  # On crée une variable qui contiendra la valeur du produit de n1 par n2, initialisée à 0
    if n2 >= 0:  # Si n2 est un nombre positif ou 0
        for _ in range(n2):  # On crée une boucle de n2 itérations
            produit += n1  # À chaque itération, on ajoute n1 à produit
    else:  # Sinon (n2 est un nombre négatif)
        for _ in range(-n2):  # On crée une boucle de -n2 itérations
            produit += -n1 # À chaque itération, on ajoute -n1 à produit
    return produit  # On renvoie la valeur de produit finale

def multiplication2(n1, n2):
    """ En une seule ligne, en utilisant les fonctions sum et abs :
    sum(liste) : Effectue la somme des éléments d'une liste, par exemple sum([3,3,3]) = 9
    abs(entier) : Renvoie la valeur absolue d'un nombre entier, par exemple abs(-5) = 5 et abs(5) = 5 """
    
    return sum([n1 if n2 >= 0 else -n1 for _ in range(abs(n2))])

# ===> EXERCICE 2 <===

def chercher(T,n,i,j):
    if i < 0 or j >= len(T) : # Si les indices i et j ne sont pas compris entre 0 et l'indice du dernier élément de T
        print("Erreur")  # Dans ce cas on affiche une erreur
        return None    # Et on renvoie None, ce qui met fin à la fonction
    if i > j :  # Si i > j, l'indice de début dépasse l'indice de fin (c-à-d qu'il n'y a plus d'élément dans la partie de T entre i et j)
        return None  # Dans ce cas on renvoie None et on met fin à la fonction
    m = (i+j) // 2  # On crée une variable m qui contient l'indice de l'élément du milieu de T
    if T[m] < n :  # Si l'élément à chercher n est plus grand que l'élément du milieu
        return chercher(T, n, m + 1, j)  # On cherche dans la partie droite
    elif T[m] > n :  # Sinon, si l'élément à chercher n est plus petit que l'élément du milieu
        return chercher(T, n, 0, m - 1)  # On cherche dans la partie gauche
    else :  # Sinon, l'élément du milieu = n
        return m  # On renvoie l'indice m
