# ===> EXERCICE 1 <===

def nb_repetitions(elt, tab):
    nb = 0  # Variable qui contiendra le nombre d'occurences de elt, initialisée à 0
    for el in tab:  # On parcourt les éléments de tab
        if el == elt:  # Si l'élément courant correspond à l'élément recherché elt
            nb += 1  # On incrémente le compteur nb
    return nb  # On renvoie enfin le compteur
        
# ===> EXERCICE 2 <===

def binaire(a):
    bin_a = str(a%2)  # bin_a est une chaîne de caractère, qui contient initialement le reste de a divisé par 2
    a = a // 2  # a prend la valeur du quotient de a par 2
    while a != 0 :  # Tant que a ne vaut pas 0 (on aurait pu aussi écrire a > 0)
        bin_a = str(a%2) + bin_a  # Ajouter le reste de la division de a par 2 au début de la chaîne bin_a
        a = a // 2  # a prend la valeur du quotient de a par 2
    return bin_a  # Renvoyer la chaîne bin_a
