# ===> EXERCICE 1 <===

def occurence_lettres(phrase):
    dic = {}  # On crée un dictionnaire initialisé à {}
    for car in phrase:  # On parcourt les caractères de phrase
        if car not in dic:  # Si le caractère rencontré n'est PAS dans le dictionnaire dic
            dic[car] = 1  # On ajoute le caractère au dictionnaire, en l'associant à un nombre d'occurences de 1
        else:
            dic[car] += 1  # On ajoute 1 occurence au nombre d'occurences du caractère car
    return dic  # On renvoie enfin le dictionnaire final

# ===> EXERCICE 2 <===
def fusion(L1,L2):
    n1 = len(L1)  # n1 contient la taille de la liste L1
    n2 = len(L2)  # n2 contient la taille de la liste L2
    L12 = [0]*(n1+n2)  # L12 prend la valeur de la somme des tailles de n1 et n2
    # On crée les indice i1, i2, i des listes L1, L2, L12, initialisés à 0 :
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2 < n2 :  # Si on a pas fini de parcourir L1, ni L2
        if L1[i1] < L2[i2]:  # Si l'élément de L1 d'indice i1 est plus petit que l'élément de L2 d'indice i2
            L12[i] = L1[i1]  # On met l'élément le plus petit des deux (L1[i1]) en position i de L12
            i1 = i1 + 1  # On incrémente l'indice i1
        else:
            L12[i] = L2[i2]  # On met l'élément le plus petit des deux (L2[i2]) en position i de L12
            i2 = i2 + 1 # On incrémente l'indice i2
        i += 1  # On incrémente l'indice i
    while i1 < n1:  # Si on a fini de parcourir L2 mais pas L1, on ajoute le reste des éléments de L1 à L12
        L12[i] = L1[i1]  # Ajout à la liste finale L12 de l'élément courant de L1
        i1 = i1 + 1  # On incrémente l'indice i1
        i = i + 1  # On incrémente l'indice i
    while i2 < n2:  # Si on a fini de parcourir L1 mais pas L2, on ajoute le reste des éléments de L2 à L12
        L12[i] = L2[i2]  # Ajout à la liste finale L12 de l'élément courant de L2
        i2 = i2 + 1  # On incrémente l'indice i2
        i = i + 1  # On incrémente l'indice i
    return L12  # On renvoie la liste finale, fusion des listes L1 et L2
