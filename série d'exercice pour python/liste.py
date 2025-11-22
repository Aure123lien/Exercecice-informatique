#Exercice création d'une liste qui va stocker des pseudos d'un jeux en ligne
#aure123lien, romain218, marthinou, Filou
online_players = ["aure123lien", "romain218", "marthinou", "Filou"]
print(online_players)
# Affiche le deuxième pseudo de la liste grace au [1]
print(online_players[1])
#Modifier un pseaudo de la liste
online_players[3]= "Filou1"
print(online_players)
#Ajouter un nouveau pseudo a la liste a une postion précise
online_players.insert(2,"Ninja")
print(online_players)
#ajouter un nouveau joueurs comme si il se connectais
online_players.append("Aurel123")
print(online_players)
#retirer un joueur si il se déconnecte
del online_players[2]
print(online_players)
