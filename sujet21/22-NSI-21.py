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

def dichotomie(tab, x):
    """
        tab : tableau d’entiers trié dans l’ordre croissant
        x : nombre entier
        La fonction renvoie True si tab contient x et False sinon
    """

    debut = 0  # Indice de début de la partie de tab dans laquelle on cherche x, initialement l'indice du premier élément
    fin = len(tab) - 1  # Indice de fin de la partie de tab dans laquelle on cherche x, initialement l'indice du dernier élément
    while debut <= fin:  # Tant que l'indice de début est plus petit ou égal à l'indice de fin (= il reste des éléments sur lesquels chercher)
        m = (debut + fin) // 2  # m contient l'indice de l'élément du milieu entre la position debut et la position fin de tab
        if x == tab[m]:  # Si l'élément cherché x correspond à l'élément du milieu (à la position m)
            return True  # L'élément est trouvé : on renvoie True
        if x > tab[m]:  # Si l'élément à chercher est plus grand que l'élément en position m (= il se situe après dans tab)
            debut = m + 1  # On change l'indice de début pour ré-effectuer la recherche à droite de m
        else:  # Sinon, cela signifie qu'il se situe avant l'élément en position m
             fin = m - 1  # On change l'indice de fin pour ré-effectuer la recherche à gauche de m
    return False  # L'élément n'a pas été trouvé : on renvoie False
