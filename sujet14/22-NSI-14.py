# ===> EXERCICE 1 <===

def correspond(mot, mot_a_trous):
    if len(mot) != len(mot_a_trous):  # Si les tailles de mot et mot_a_trous sont différentes
        return False  # On renvoie False
    # Si les deux mots sont bien de la même taille :
    for i in range(len(mot)):  # Parcourir la liste mot (et mot_a_trous)
        if mot_a_trous[i] != '*':  # Si le caractère de mot_a_trous n'est pas *
            if mot_a_trous[i] != mot[i]:  # Si la lettre de mots_a_trous ne correspond pas à celle de mot
                return False  # Dans ce cas on renvoie False
    return True  # Si toutes les lettres (or trous) correspondent, on renvoie True

# ===> EXERCICE 2 <===

def est_cyclique(plan):
    '''
    Prend en paramètre un dictionnaire `plan` correspondant 
    à un plan d'envoi de messages entre `N` personnes A, B, C, 
    D, E, F ...(avec N <= 26).
    Renvoie True si le plan d'envoi de messages est cyclique
    et False sinon. 
    '''
    personne = 'A'  # On prend A comme personne de départ
    N = len(plan)  # N contient la taille du dictionnaire plan                      
    for i in range(N - 1):  # On regarde les N - 1 successeurs de A
        if plan[personne] == 'A':  # Si on retombe sur la personne A
            return False  # Le plan n'est donc pas cyclique
        else:  # Sinon
            personne = plan[personne]  # La personne courante devient le successeur de la personne précédente
    return True  # On n'est pas retombé sur 'A' : On renvoie True
