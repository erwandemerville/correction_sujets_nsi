# ===> EXERCICE 1 <===

def recherche(tab, n):
    deb = 0  # deb contient l'indice de début de tab
    fin = len(tab) - 1  # deb contient l'indice de fin de tab
    while deb <= fin:  # Tant que l'indice du début est inférieur à l'indice de fin
        milieu = (fin + deb) // 2  # Contient l'indice du milieu de tab entre les indices deb et fin
        if tab[milieu] == n:  # Si l'élément du milieu correspond à n
            return milieu  # On renvoie l'élément du milieu
        else:
            if n < tab[milieu]:  # Si n est situé AVANT l'élément du milieu dans la liste
                fin = milieu - 1  # On change l'indice de fin de la liste pour prendre la partie gauche
            else:  # Si n est situé APRES l'élément du milieu dans la liste
                deb = milieu + 1  # On change l'indice de début de la liste pour prendre la partie droite
    return -1  # Finalement, on renvoie -1 si l'élément n'a pas été trouvé
    
# ===> EXERCICE 2 <===

ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ALPHABET.find(lettre)

def cesar(message, decalage):
    resultat = ''  # Chaîne de caractères qui contiendra le message final
    for lettre in message :  # On parcourt chaque lettre du message
        if lettre in ALPHABET :  # Si la lettre courante est présente dans ALPHABET
            indice = ( position_alphabet(lettre) + decalage )%26  # Voir note 1 en dessous
            resultat = resultat + ALPHABET[indice]  # On ajoute la lettre à resultat avec le décalage
        else:  # Si la lettre n'est pas dans l'ALPHABET
            resultat = resultat + lettre  # On ajoute la lettre sans la changer
    return resultat

# Note 1 : indice contient l'indice de la lettre de ALPHABET décalée par rapport à la lettre initiale.
# Le '%26' permet de faire en sorte que si on dépasse la lettre Z, on revienne à la lettre A.
# Par exemple : 'Z' avec un décalage de 2 donnerait 27 % 26 = 1, on retombe donc sur la lettre 'B'.