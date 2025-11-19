#Les fonctions mathématiques

def addition(a, b):
    #Retourne la somme des deux nombres
    return a + b

def soustraction(a, b):
    #Retourne la différence des deux nombres
    return a - b

def multiplication(a, b):
    #Retourne le produit des deux nombres
    return a * b

def division(a, b):
    #Vérifie si la personne essaie de diviser par zéro
    if b == 0:
        return "Erreur : division par zéro"
    #Retourne le résultat de la division
    return a / b


#Fonction principale du programme