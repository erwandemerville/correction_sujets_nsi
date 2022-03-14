# ===> EXERCICE 1 <===

def rendu(somme_a_rendre):
    rend = [0, 0, 0]  # Liste qui contiendra le nb de billets de 5, pièces de 2 et de 1, initialisée à [0,0,0]
    rend[0] = somme_a_rendre // 5  # Le nombre de billets de 5 correspond au quotient de somme_a_rendre par 5
    somme_a_rendre = somme_a_rendre % 5  # La nouvelle somme_a_rendre est le reste de somme_a_rendre par 5
    rend[1] = somme_a_rendre // 2  # Même principe pour les pièces de 2
    somme_a_rendre = somme_a_rendre % 2
    rend[2] = somme_a_rendre // 1  # Enfin, on divise par 1 pour connaître le nombre de pièces de 1 nécessaire
    return rend
        
# ===> EXERCICE 2 <===

class Maillon :
    def __init__(self,v) :
        self.valeur = v
        self.suivant = None

class File :
    def __init__(self) :
        self.dernier_file = None

    def enfile(self,element) :
        nouveau_maillon = Maillon(element)  # On crée un nouveau Maillon de valeur element 
        nouveau_maillon.suivant = self.dernier_file  # L'ancien dernier maillon devient le maillon suivant le nouveau
        self.dernier_file = nouveau_maillon   # Le nouveau maillon devient le dernier ajouté à la file

    def est_vide(self) :
        return self.dernier_file == None

    def affiche(self) :
        maillon = self.dernier_file
        while maillon != None :  # Tant qu'il reste un maillon à afficher
            print(maillon.valeur)  # On affiche le maillon
            maillon = maillon.suivant  # Puis on passe au maillon suivant

    def defile(self) :
        if not self.est_vide() :  # Si la file n'est pas vide
            if self.dernier_file.suivant == None :  # Si aucun maillon ne suit le dernier maillon ajouté
                resultat = self.dernier_file.valeur  #  Le resultat devient la valeur du dernier maillon de la file
                self.dernier_file = None  # On supprime de la file l'unique maillon présent
                return resultat  # Et on renvoie la valeur du maillon
            # Si la fonction continue, cela signifie qu'il y a plus d'un maillon dans la file
            maillon = self.dernier_file  # Le maillon courant devient le dernier maillon ajouté
            while maillon.suivant.suivant != None :  # Tant qu'il reste un maillon qui suit le maillon suivant
                                                     # Autrement dit, on s'arrête au deuxième élément de la file
                maillon = maillon.suivant  # Le maillon courant devient le maillon qui suit l'ancien
            resultat = maillon.suivant.valeur  # Boucle finie, on prend la valeur du premier maillon de la file
            maillon.suivant = None  # Deuxième maillon de la file devient le premier, on supprime le premier maillon
            return resultat  # On renvoie la valeur du premier maillon de la file (celui qui a été supprimé)
        return None # La file est vide : On renvoie None
