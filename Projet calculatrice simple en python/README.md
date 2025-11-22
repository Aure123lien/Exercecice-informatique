# Calculatrice simple en Python

Ce projet est une calculatrice en Python qui permet de réaliser des opérations simples : addition, soustraction, multiplication et division.  
Le programme prend en compte les erreurs de saisie et gère la division par zéro pour offrir une expérience a l'utilisation qui sera fiable et avec aucune erreur du programme lors de l'utlisation par quelqu'un


# Objectif du projet
Ce projet a été réalisé pour mon dossier Parcoursup, afin de montrer ma compréhension des bases de la programmation en Python.  
Il a pour but de vous montrer mes compétences dans :  

- L’utilisation et la création de fonctions pour structurer le code  
- L’utilisation des boucles pour répéter des actions et permettre la continuité du programme  
- La gestion des erreurs grâce aux blocs try/except  
- La manipulation de la saisie de la personne et l’utilisation des conditions 


# Fonctionnalités

Le programme permet à l’utilisateur de :  

1. Saisir deux nombres de son choix  
2. Choisir l’opération à effectuer parmi `+`, `-`, `*`, `/`  
3. Calculer le résultat et l’afficher immédiatement  
4. Recommencer un nouveau calcul ou quitter le programme selon son choix  

Le programme se termine automatiquement lorsque la personne indique qu’il n'a plus besoin de faire un autre calcul


# Structure du code

Le code est organisé autour de plusieurs fonctions pour avoir les opérations voulue :  

- addition(a, b) : calcule la somme de deux nombres  
- soustraction(a, b)` : calcule la différence entre deux nombres  
- multiplication(a, b) : calcule le produit de deux nombres  
- division(a, b) : calcule le quotient de deux nombres en vérifiant que le diviseur n’est pas egale a zéro  

La fonction principale calculatrice() :  
- Demande les saisies des nombres a la personne  
- Vérifie la validité des entrées avec try/except  
- Demande de bien choisir une opération qui est voulue
- Affiche le résultat et propose de refaire un calcul  

Cette structure permet de rendre le code lisible, modulable et facile à maintenir.  


# Contexte du projet

J’ai choisi de réaliser cette calculatrice pour apprendre à structurer un programme Python, gérer les erreurs et rendre le code interactif.  
Ce projet m’a permis de :  

- Comprendre comment utiliser des fonctions pour éviter la répétition de code   
- Appliquer des boucles pour rendre l’application continue ou de s"arreter dés que la personne n'en a plus besoin 
- Mettre en pratique la gestion des erreurs pour permettre une meilleur utilisation et utilité au programme  
- Améliorer la lisibilité et l’organisation du code  


# Difficultés rencontrées

- Gestion de la division par zéro  
- Vérification que l’utilisateur saisit bien des nombres  
- Compréhension des boucles et de la logique

Grâce à ces difficultés, j’ai appris à anticiper les erreurs que je pouvais faire a ce moment 


# Améliorations possibles

- Ajouter des opérations avancées comme la puissance, la racine carrée 
- Enregistrer un historique des calculs dans un fichier pour le regarder a un autre moment
- Ajouter la possibilité de gérer plusieurs calculs en chaîne en meme temps  


# Conclusion

Ce projet m’a permis de consolider mes bases en Python,Il va constituer un premier projet concret vers des projets plus complexes