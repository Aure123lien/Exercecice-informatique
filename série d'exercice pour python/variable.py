# recolter une valeur du porte monnaie
wallet = int(input("Entrer le nombre d'argent que vous avez"))
print("Vous avez actuellement", wallet, "euros")
 
# creer un produit qui aura pour valeur 60 euros
produit = 60
print("Le Produit vaut ", produit, "euros")
 
# enleve au "wallet" le prix du produit
wallet = wallet - produit

# afficher la nouvelle valeur du porte monnaie
print("Le produit a bien été acheté ")
print("Il ne vous reste plus que", wallet, "euros")
