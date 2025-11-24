import pygame
pygame.init()
from game import Game

# on va générer la fenêtre du jeu
pygame.display.set_caption("Jeu de tir en 2D")
screen = pygame.display.set_mode((1080, 720))

# On va importer une image pour le mettre en arrière-plan du jeu
background = pygame.image.load("Projet jeux python en 2D/assets/Background.jpg").convert()

# charger le jeu
game = Game()

running = True

# On va créer une boucle pour la condition juste au-dessus
while running:

    # appliquer l'arrière-plan
    screen.blit(background, (0, 0))

    # appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    # afficher barre de vie joueur
    game.player.update_health_bar(screen)

    # recuperer le projectile envoyer par le joueurr
    for projectile in game.player.all_projectiles:
        projectile.move()

    # recuperer le monstre actuellement dans le jeu
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # je vais appliquer l'ensemble des images
    game.player.all_projectiles.draw(screen)

    # appliquer l'image du groupe monstre que j'ai créer
    game.all_monsters.draw(screen)

    # Deplacement de mon joueur veut aller a gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width() :
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    # SUPPRIMÉ : print(game.player.rect.x)

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

                

