import pygame
pygame.init()
import math
from game import Game

# Réaliser une clock
clock = pygame.time.Clock()
FPS = 120

# on va générer la fenêtre du jeu
pygame.display.set_caption("Jeu de tir en 2D")
screen = pygame.display.set_mode((1080, 720))

# On va importer une image pour le mettre en arrière-plan du jeu
background = pygame.image.load("Projet jeux python en 2D/assets/Background.jpg").convert()

# charger la bannière
banner = pygame.image.load("Projet jeux python en 2D/assets/banner.png").convert_alpha()
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# charger le bouton jouer
play_button = pygame.image.load("Projet jeux python en 2D/assets/button.png").convert_alpha()
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 1.8)


# charger le jeu
game = Game()

running = True

# On va créer une boucle pour la condition juste au-dessus
while running:

    # appliquer l'arrière-plan
    screen.blit(background, (0, 0))

    # vérifier si le jeu a commencé
    if game.is_playing:
        # déclencher les informations de la partie
        game.update(screen)
    # si le jeux n'a pas commencer
    else:
        # afficher l'écran d'acceuil
        screen.blit(banner, banner_rect)
        screen.blit(play_button, play_button_rect)

    # Mettre à jour l'écran
    pygame.display.flip()

    # On va vérifier si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        # On va vérifier si l'événement est la fermeture de la fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Le jeu se ferme")

        # je vais detecter si un joueur fais une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # Création d'une activité pour la touche espace
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # la souris touche le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # lancer le jeux
                game.start()
    # fixer le nombre de FPS
    clock.tick(FPS)
                

