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

def main():
    # Message de début de la calculatrice
    print("=== Calculatrice Python ===")
    print("Opérations disponibles : +  -  *  /")
    
    #Boucle infinie pour permettre plusieurs calculs d'affilée
    while True:
        try:
            #Demande le premier nombre à la personne
            a = float(input("Entrez le premier nombre : "))
            #Demande le second nombre
            b = float(input("Entrez le second nombre : "))
        except ValueError:
            #Message d'erreur si la personne ne met pas un nombre
            print("Veuillez entrer uniquement des nombres.")
            continue  # Retour à la boucle pour recommencer
if __name__ == "__main__":
    main()