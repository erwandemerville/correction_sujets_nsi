# ===> EXERCICE 1 <===

def calcul(n):
    lst = [n]  # Variable qui contiendra la liste des éléments finale, initialisée à une liste contenant juste n
    while n != 1:  # Tant que n n'est pas égal à 1
        if n % 2 == 0:  # Si l'élément n est pair :
            n = int(n / 2)  # n prend la valeur de la division de n par 2 (convertie en entier)
        else:  # Sinon :
            n = 3*n + 1  # n prend la valeur 3*n + 1 
        lst.append(n)  # On ajoute à lst la nouvelle valeur de n
    return lst  # On renvoie enfin la liste des éléments finale
    
# ===> EXERCICE 2 <===

dico = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, \
        "H":8, "I":9, "J":10, "K":11, "L":12, "M":13, \
        "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, \
        "T":20, "U":21,"V":22, "W":23, "X":24, "Y":25, "Z":26}

def est_parfait(mot) :
    # mot est une chaîne de caractères (en lettres majuscules)
    code_c = ""  # code_c contiendra la suite des codes des lettres du mot
    code_a = 0  # code_a contiendra la somme des codes des lettres du mot, initialisée à 0
    for c in mot :  # On parcourt chaque caractère du mot
        code_c = code_c + str(dico[c])  # On concatène code_c avec le code associé à la lettre c (convertie en 'str')
        code_a = code_a + dico[c]  # On ajoute à code_a l'entier correspondant à la lettre c
    code_c = int(code_c)  # On convertit code_c en entier
    if not code_c % code_a :  # Si le reste de la division de code_c par code_a vaut 0
        mot_est_parfait = True  # Dans ce cas, le mot est parfait
    else :  # Sinon
        mot_est_parfait = False  # Le mot n'est pas parfait
    return [code_a, code_c, mot_est_parfait]  # On renvoie une liste contenant le code_a, code_c et True ou False
