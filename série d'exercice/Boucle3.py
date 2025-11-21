# Importer la fonction randint
from random import randint

# Générer le nombre mystère entre 1 et 100
nombre_mystere = randint(1, 100)

# Compteur d'essais
nombre_essais = 0

print("Bienvenue au jeu du juste prix ! Essaie de deviner le nombre mystère entre 1 et 100.")

# Boucle principale du jeu
while True:
    # Demander à l'utilisateur de saisir un nombre
    proposition = int(input("Ton estimation : "))
    nombre_essais += 1
    
    # Vérifier si l'utilisateur a trouvé le prix
    if proposition == nombre_mystere:
        print(f"Félicitations ! Tu as trouvé le nombre mystère en {nombre_essais} essais.")
        break
    elif proposition > nombre_mystere:
        print("C'est moins ! Essaie encore.")
    else:
        print("C'est plus ! Essaie encore.")

print("Merci d'avoir joué !")