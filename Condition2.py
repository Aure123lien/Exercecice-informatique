# Récolter l'age de la personne "quel est votre age ?"
age =int(input("Quel est votre âge ? "))
print(age)
#si la personne est mineur la place coute 8 euros
#si la personne est majeur la place coute 12 euros
if age < 18:
    prix_place = 8
else:
    prix_place = 12
#souhaitez vous du popcorn
popcorn_request = input("Souhaitez-vous prendre du popcorn?")
#si oui ajouter 3 euros au prix de la place
if popcorn_request == "oui":
    prix_place += 3 
#afficher le prix total a payer pour le cinéma
print("Le prix total à payer est de", prix_place, "euros.")