# ===> EXERCICE 1 <===

# Méthode 1 :
def conv_bin(n):
    ''' Renvoie un couple (b, bit) contenant la représentation binaire de n
    et le nombre de bits constituant b.
    :param n: (int) Entier positif
    :return (tuple): Couple (b, bit) '''
    
    b = []  # On crée une liste b qui contiendra la représentation binaire de n, initialement vide
    while n != 0:  # Tant que n est différent de 0 (on aurait pu aussi écrire > 0)
        b = [n % 2] + b  # On ajoute le reste de la division n par 2 au début de b
        n = n // 2  # On remplace n par le quotient de la division n par 2
    return b, len(b)  # Retourne un couple (tuple) contenant b et le nombre de bits (= taille de b)

# Méthode 2 (avec append et reverse) :
def conv_bin2(n):
    b = []  # On crée une liste b qui contiendra la représentation binaire de n, initialement vide
    while n != 0:  # Tant que n est différent de 0 (on aurait pu aussi écrire > 0)
        b.append(n % 2) # On ajoute le reste de la division n par 2 à la fin de la liste b
        n = n // 2  # On remplace n par le quotient de la division n par 2
    b.reverse()  # On inverse la liste b avec la fonction reverse
    return b, len(b)  # Retourne un couple (tuple) contenant b et le nombre de bits (= taille de b)

# Une autre méthode :
def conv_bin3(n):
    b = list(bin(n)[2:])  # On utilise la fonction bin pour convertir en binaire, on met sous forme d'une liste
                          # On ne prend pas les deux premiers caractères '0b' qui indiquent que la notation est binaire
    b = [int(el) for el in b]  # On convertit les éléments de la liste en entiers (car ce sont des 'str' à la base)
    return b, len(b)  # On renvoie enfin la liste b et sa taille

# ===> EXERCICE 2 <===

def tri_bulles(T):
    n = len(T)  # n prend comme valeur la taille de T
    for i in range(n - 1, 0, -1):  # On parcourt la liste T du dernier au deuxième élément (indice 1) avec un pas de -1
        for j in range(i):  # On parcourt la liste de l'indice 0 jusqu'à i - 1
            if T[j] > T[j + 1]:  # Si l'élément d'indice j est plus grand que l'élément qui le suit
                # Les 3 lignes suivantes permettent d'effectuer la permutation
                temp = T[j]  # On stocke dans une variable temp la valeur de la liste à l'indice j
                T[j] = T[j + 1]  # À la position j de la liste, on met l'élément qui le suit
                T[j+1] = temp  # Enfin, on met le contenu de temp à l'indice j + 1
    return T  # On renvoie la liste triée
