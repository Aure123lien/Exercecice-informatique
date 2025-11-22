#for : pour une valeur de départ, jusqu'a une valeur d'arrivée
for num_client in range(1, 8):
    print("Vous etes le client n°", num_client)

# on va lister des emails
email = ["aurelien@gmail.com", "aurelien1@gmail.com", "aurelien2@gmail.com"]

#création d'une blacklist
blacklist = ["aurelien@gmail.com"]

for mail in email:

    if mail in blacklist:
        print("Email {} sera refusé".format(mail))
        continue

    print("Email {} sera accepté".format(mail))