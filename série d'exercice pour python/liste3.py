text = input("entrez une chaine de la forme (email-pseaudo-motdepasse)").split("-")
print(text)

print("salut {}, ton email {}".format(text[1], text[0]))
