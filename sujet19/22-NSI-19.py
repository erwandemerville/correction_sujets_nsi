# ===> EXERCICE 1 <===

def multiplication(n1, n2):
    produit = 0  # On crée une variable qui contiendra le produit, initialisée à 0
    signe = 1  # On crée une variable pour indiquer le signe de n1, 1 si positif, -1 si négatif, initialement à 1
    if n1 < 0:  # Si n1 est un nombre négatif
        signe = -1  # On indique dans la variable signe que le signe de n1 est négatif
        n1 = -n1  # On transforme n1 en nombre positif
    for _ in range(n1):  # On fait une boucle de n1 itérations 
        produit += n2  # Puis on ajoute n2 à produit à chaque itération
    return signe * produit  # On renvoie produit, en le multipliant par signe pour que le bon signe soit associé

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
