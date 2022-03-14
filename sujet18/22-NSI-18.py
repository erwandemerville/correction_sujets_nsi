# ===> EXERCICE 1 <===

def mini(releve, date):
    minimum = None  # On crée une variable qui contiendra la température minimale, initialisée à None
    for i in range(len(releve)):  #  On parcourt les températures de releve
        if not minimum or releve[i] < minimum:  # Si minimum est à None ou que la température d'indice i est plus petite que minimum
            minimum = releve[i]  # Le nouveau minimum devient la température d'indice i
            annee = date[i]  # Et la variable annee prend la valeur de l'année correspondante à la température minimale
    return minimum, annee  # On retourne le minimum et l'année

# ===> EXERCICE 2 <===

def inverse_chaine(chaine):
    result = ''  # On crée une chaîne vide
    for caractere in chaine:  # On parcourt chaque caractère de la chaîne chaine
       result = caractere + result  # On place le caractère courant au début de la chaîne result
    return result  # Puis on renvoie la chaîne inversée

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return chaine == inverse  # Si la chaîne et son inverse sont équivalentes, renvoie True, False sinon
    
def est_nbre_palindrome(nbre):
    chaine = str(nbre)  # On convertit le nombre (type int) en chaîne de caractère (type str) avec la fonction str
    return est_palindrome(chaine)  # Puis on appelle est_palindrome pour vérifier si la chaine est un palindrome
