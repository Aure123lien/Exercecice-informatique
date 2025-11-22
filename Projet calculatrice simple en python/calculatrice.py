# Calculatrice simple en Python

# Fonctions pour les opérations
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Erreur : division par zéro impossible."
    return a / b

#Fonction principale du programme
def calculatrice():
    print("Calculatrice Python")
    
    while True:
        # Demande des nombres à la personne
        try:
            x = float(input("Entrez le premier nombre : "))
            y = float(input("Entrez le deuxième nombre : "))
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.\n")
            continue

        # Choix de l'opération a utiliser
        operation = input("Choisissez une opération (+, -, *, /) : ")

        # Calcul selon l'opération que la personne a choisie
        if operation == "+":
            resultat = addition(x, y)
        elif operation == "-":
            resultat = soustraction(x, y)
        elif operation == "*":
            resultat = multiplication(x, y)
        elif operation == "/":
            resultat = division(x, y)
        else:
            print("Erreur : opération non reconnue.\n")
            continue

        print(f"Résultat : {resultat}")

        # Demander si on recommence un autre calcul
        continuer = input("Voulez-vous faire un autre calcul ? (oui/non) : ").lower()
        if continuer != "oui":
            print("Merci d'avoir utilisé la calculatrice !")
            break

calculatrice()

