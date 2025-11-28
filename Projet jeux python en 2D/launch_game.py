
# Lanceur de mon jeu Python en 2D

import sys
import os

# Ajouter le répertoire actuel pour l'envoi
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)
os.chdir(current_dir)  # Changer le répertoire de travail

# Importer et lancer le jeu
try:
    from main.main import *
except ImportError as e:
    print(f"Erreur lors du lancement du jeu : {e}")
    print("Assurez-vous que tous les fichiers sont présents dans la structure correcte.")
    print("Si le problème persiste, essayez : python -m main.main")
    input("Appuyez sur Entrée pour quitter...")
    sys.exit(1)