# ===> EXERCICE 1 <===

def moyenne(liste):
    numerateur = 0  # On crée une variable qui stockera la somme des notes multipliées par leur coefficient, initialisée à 0
    denominateur = 0  # On crée une variable qui stockera la somme des coefficients, initialisée à 0
    for couple in liste:  # On parcourt chaque couple (note, coefficient) de notre liste
        note = couple[0]  # On stocke dans une variable note le premier élément du couple
        coefficient = couple[1]  # On stocke dans une variable coefficient le deuxième élément du couple
        numerateur += note * coefficient  # On ajoute au numérateur le produit entre la note et le coefficient du couple
        denominateur += coefficient  # On ajoute au dénominateur le coefficient du couple
    return numerateur / denominateur  # On renvoie la moyenne calculée en divisant le numérateur par le dénominateur

# ===> EXERCICE 2 <===

# Note : Cet exercice n'est pas si facile.
# Pour vous simplifier la vie, je vous conseille de représenter le triangle de pascal
# sous forme d'un tableau à deux dimensions, en indiquant les indices en ligne et en colonne. (0, 1, 2, ...)

def pascal(n):
    C = [[1]]  # C contiendra notre liste finale, on l'initialise avec la première ligne du triangle de pascal
    for k in range(1, n + 1):  # k (numéro de la ligne) prend une valeur allant de 1 à n
        Ck = [1]  # Ck contiendra la ligne k, initialisée à [1] car une ligne commence toujours par 1
        for i in range(1,k):  # On parcourt chaque colonne de la ligne k, i prend la valeur de la colonne courante
            Ck.append(C[k-1][i-1]+C[k-1][i])  # On fait la somme des deux éléments juste au dessus
        Ck.append(1)  # On ajoute 1 car une ligne finit toujours par 1
        C.append(Ck)  # On ajoute la ligne courante à C
    return C  # On retourne le triangle de pascal ainsi créé
