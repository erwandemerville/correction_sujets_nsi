# ===> EXERCICE 1 <===

# Méthode 1
def renverse(chaine):
    nouvelle_chaine = ''  # On crée une nouvelle chaîne vide, qui contiendra le mot final inversé
    for car in chaine:  # On parcourt chaque caractère de chaine
        nouvelle_chaine = car + nouvelle_chaine  # On met le caractère au début de nouvelle_chaine
    return nouvelle_chaine  # Enfin, on renvoie la chaîne inversée

# Méthode 2 (avec slicing)
def renverse2(chaine):
    return chaine[::-1]  # On renvoie une nouvelle chaine qui copie les caractères de chaine du dernier jusqu'au premier, avec un pas de -1

# ===> EXERCICE 2 <===

def crible(N):
    """renvoie un tableau contenant tous les nombres premiers plus petits que N"""
    premiers = []  # On crée un tableau vide qui contiendra tous les nombres premiers plus petits que N
    tab = [True] * N  # On crée un tableau tab de N valeurs initialisées à True
    tab[0], tab[1] = False, False  # 0 et 1 ne sont pas premiers, on les associe donc à la valeur False dans tab
    for i in range(2, N):  # On parcourt les nombres premiers de 2 à N - 1
        if tab[i] == True:  # Si i est un nombre premier, c'est-à-dire que l'élément de tab d'indice i vaut True
            premiers.append(i)  # On ajoute i dans le tableau des nombres premiers
            for multiple in range(2*i, N, i):  # On parcourt tous les multiples de i jusqu'à N - 1
                tab[multiple] = False  # Et on indique que ces multiples ne sont pas premiers en mettant la valeur dans tab à False
    return premiers  # On renvoie enfin le tableau des nombres premiers

assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
