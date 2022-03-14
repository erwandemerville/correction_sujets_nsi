# ===> EXERCICE 1 <===

def recherche(caractere, mot):
    nb_caracteres = 0  # Variable stockant le nombre de caractères trouvé, initialisée à 0
    for c in mot:  # On parcourt chaque caractère du mot passé en argument
        if c == caractere:  # Si le caractère courant est égal au caractère recherché
            nb_caracteres += 1  # On incrémente nb_caracteres
    return nb_caracteres  # Enfin, on retourne le nombre de caractères trouvé

# ===> EXERCICE 2 <===

Pieces = [100,50,20,10,5,2,1]

def rendu_glouton(arendre, solution=[], i=0):
    if arendre == 0:  # Le cas de base (quand on a plus rien à rendre)
        return solution  # Lorsqu'on a plus rien à rendre, on retourne la solution
    p = Pieces[i]  # p prend la valeur de la pièce d'indice i
    if p <= arendre :  # Si la somme à rendre est supérieur à la pièce d'indice i
        solution.append(p)  # Dans ce cas on ajoute cette pièce dans la solution
        return rendu_glouton(arendre - p, solution, i)  # On soustrait la valeur de la pièce à la somme à rendre
    else :  # Sinon on n'ajoute pas la pièce dans la solution, et on passe à la pièce suivante
        return rendu_glouton(arendre, solution, i + 1)  # On rappelle l'algo en passant à la pièce d'indice i + 1
