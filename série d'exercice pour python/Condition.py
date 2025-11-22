#Exercice 1: Système de mot de passe
password = input("Entrez le mot de passe")
password_length = len(password)
print(password_length)

#Verifier si le mot de passe est inférieur a 6 caractères
if password_length < 6:
    print("le mot de passe est trop court saisiser un mot de passe plus long")
elif password_length > 10 and password_length <= 15:
    print("le mot de passe moyen")
else:
    print("le mot de passe parfait")
