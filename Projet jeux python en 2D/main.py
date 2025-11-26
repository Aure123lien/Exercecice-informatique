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

# charger l’image de fin de partie
game_over_img = pygame.image.load("Projet jeux python en 2D/assets/Game_over.png").convert_alpha()
game_over_img = pygame.transform.scale(game_over_img, (1080, 720))
go_rect = game_over_img.get_rect()

# charger le jeu
game = Game()

# Fonts
title_font = pygame.font.Font("Projet jeux python en 2D/assets/CustomFont.ttf", 60)
text_font = pygame.font.Font("Projet jeux python en 2D/assets/CustomFont.ttf", 35)

# Zones cliquables
restart_rect = pygame.Rect(400, 270, 350, 60)
menu_rect = pygame.Rect(400, 350, 350, 60)

running = True

while running:

    # appliquer l'arrière-plan
    screen.blit(background, (0, 0))

    # vérifier si le jeu a commencé
    if game.is_playing:
        game.update(screen)

    else:
        # écran d'accueil
        if not game.is_game_over:
            screen.blit(banner, banner_rect)

            # sensation de survol sur le bouton jouer du menu principale
            mouse_pos = pygame.mouse.get_pos()

            if play_button_rect.collidepoint(mouse_pos):
                hovered_play = pygame.transform.scale(play_button, (430, 160))
                hovered_rect = hovered_play.get_rect(center=play_button_rect.center)
                screen.blit(hovered_play, hovered_rect)
            else:
                screen.blit(play_button, play_button_rect)

        # écran de fin de partie
        else:
            screen.blit(game_over_img, go_rect)

            # Titre
            title = title_font.render("Vous avez péri", True, (255, 0, 0))
            screen.blit(title, title.get_rect(center=(540, 120)))

            # Gestion du survol Game Over
            mouse_pos = pygame.mouse.get_pos()

            # bouton recommencer
            if restart_rect.collidepoint(mouse_pos):
                color = (255, 255, 0)
                hover_font = pygame.font.Font("Projet jeux python en 2D/assets/CustomFont.ttf", 40)
                text = hover_font.render("Recommencer une nouvelle partie", True, color)
            else:
                text = text_font.render("Recommencer une nouvelle partie", True, (255, 255, 255))

            screen.blit(text, text.get_rect(center=restart_rect.center))

            # bouton retour au menu principale
            if menu_rect.collidepoint(mouse_pos):
                color = (255, 255, 0)
                hover_font = pygame.font.Font("Projet jeux python en 2D/assets/CustomFont.ttf", 40)
                text = hover_font.render("Retour au menu principale", True, color)
            else:
                text = text_font.render("Retour au menu principale", True, (255, 255, 255))

            screen.blit(text, text.get_rect(center=menu_rect.center))

    pygame.display.flip()

    # gestions des évenements
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Le jeu se ferme")

        # touche espace pour tirer
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game.is_playing:
                game.player.launch_projectile()

            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = event.pos

            # bouton jouer
            if not game.is_playing and not game.is_game_over:
                if play_button_rect.collidepoint(mouse_pos):
                    game.start()
                    game.sound_manager.play("click")

            # bouton fin de partie
            if game.is_game_over:

                # recommencer
                if restart_rect.collidepoint(mouse_pos):
                    game.is_game_over = False
                    game.start()
                    game.sound_manager.play("click")

                # retour au menu
                elif menu_rect.collidepoint(mouse_pos):
                    game.is_game_over = False
                    game.is_playing = False
                    game.sound_manager.play("click")

    clock.tick(FPS)







