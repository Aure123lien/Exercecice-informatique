import pygame
import sys
import math
pygame.init()

# Musique du menu
pygame.mixer.music.load("Projet jeux python en 2D/assets/sounds/musique_ecran_d'acceuil.ogg")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, fade_ms=50)

from game import Game

# Réaliser une clock
clock = pygame.time.Clock()
FPS = 120

# Musique du jeu
game_music_path = "Projet jeux python en 2D/assets/sounds/musique_dans_le_jeux.ogg"

# Menu pause
is_paused = False

# Fenêtre du jeu
pygame.display.set_caption("Jeu de tir en 2D")
screen = pygame.display.set_mode((1920, 1080))

# Arrière-plan
background = pygame.image.load("Projet jeux python en 2D/assets/Background.jpg").convert()
background = pygame.transform.scale(background, (1920, 1080))

# Bannière
banner = pygame.image.load("Projet jeux python en 2D/assets/banner.png").convert_alpha()
banner = pygame.transform.scale(banner, (int(screen.get_width()*0.42), int(screen.get_height()*0.7)))
banner_rect = banner.get_rect()
banner_rect.centerx = screen.get_width() // 2
banner_rect.y = int(screen.get_height() * 0.05)

# Bouton jouer
play_button = pygame.image.load("Projet jeux python en 2D/assets/button.png").convert_alpha()
play_button = pygame.transform.scale(play_button, (int(screen.get_width()*0.25), int(screen.get_height()*0.14)))
play_button_rect = play_button.get_rect()
play_button_rect.centerx = screen.get_width() // 2
play_button_rect.y = int(screen.get_height() / 1.6)
play_button_hover = pygame.transform.scale(play_button, (int(screen.get_width()*0.27), int(screen.get_height()*0.15)))
play_button_hover_rect = play_button_hover.get_rect(center=play_button_rect.center)

# Bouton crédits
credits_img_original = pygame.image.load("Projet jeux python en 2D/assets/credits.png").convert_alpha()
credits_img = pygame.transform.scale(credits_img_original, (int(screen.get_width()*0.12), int(screen.get_height()*0.07)))
credits_rect = credits_img.get_rect(topright=(screen.get_width()-20, 20))
credits_img_hover = pygame.transform.scale(credits_img_original, (int(screen.get_width()*0.135), int(screen.get_height()*0.08)))
credits_hover_rect = credits_img_hover.get_rect(center=credits_rect.center)

# Bouton quitter
quit_img_original = pygame.image.load("Projet jeux python en 2D/assets/quit.png").convert_alpha()
quit_img = pygame.transform.scale(quit_img_original, (int(screen.get_width()*0.25), int(screen.get_height()*0.14)))
quit_rect = quit_img.get_rect()
quit_rect.centerx = screen.get_width() // 2
quit_rect.y = play_button_rect.y + play_button_rect.height + 20
quit_img_hover = pygame.transform.scale(quit_img, (int(screen.get_width()*0.27), int(screen.get_height()*0.15)))
quit_hover_rect = quit_img_hover.get_rect(center=quit_rect.center)

# Popup crédits
show_popup = False
popup_width = int(screen.get_width() * 0.3)
popup_height = int(screen.get_height() * 0.28)
popup_rect = pygame.Rect((screen.get_width() - popup_width)//2,
                         (screen.get_height() - popup_height)//2,
                         popup_width,
                         popup_height)
close_btn_radius = 18
close_btn_center = (popup_rect.right - 30, popup_rect.top + 30)

# Fonts
title_font = pygame.font.Font("Projet jeux python en 2D/assets/CustomFont.ttf", 60)
text_font = pygame.font.Font("Projet jeux python en 2D/assets/CustomFont.ttf", 35)
credit_font = pygame.font.Font("Projet jeux python en 2D/assets/CustomFont.ttf", 30)
pause_font = pygame.font.Font("Projet jeux python en 2D/assets/CustomFont.ttf", 50)

# Zones cliquables fin de partie
restart_rect = pygame.Rect(int(screen.get_width()*0.21), int(screen.get_height()*0.25), int(screen.get_width()*0.18), int(screen.get_height()*0.055))
menu_rect = pygame.Rect(int(screen.get_width()*0.21), int(screen.get_height()*0.32), int(screen.get_width()*0.18), int(screen.get_height()*0.055))

# Charger le jeu
game = Game()

# Timer de manche
manche_start_time = 0

running = True

while running:

    screen.blit(background, (0, 0))
    mouse_pos = pygame.mouse.get_pos()

    # Partie en cours
    if game.is_playing:
        if not is_paused:
            game.update(screen)

            # Score au centre supérieur
            score_text = text_font.render(f"Score : {game.player.score}", True, (255, 255, 255))
            score_rect = score_text.get_rect(center=(screen.get_width()//2, 50))
            screen.blit(score_text, score_rect)

            # Timer de manche
            elapsed_time = (pygame.time.get_ticks() - manche_start_time) // 1000
            timer_text = text_font.render(f"Temps : {elapsed_time}s", True, (255, 255, 255))
            timer_rect = timer_text.get_rect(topleft=(20, 20))
            screen.blit(timer_text, timer_rect)

        else:
            # Overlay menu pause
            overlay = pygame.Surface((1920, 1080), pygame.SRCALPHA)
            overlay.fill((0,0,0,150))
            screen.blit(overlay,(0,0))

            pause_rect = pygame.Rect(screen.get_width()//2 - 250, screen.get_height()//2 - 100, 500, 200)
            pygame.draw.rect(screen, (50,50,50), pause_rect, border_radius=12)
            pygame.draw.rect(screen, (255,255,255), pause_rect, width=3, border_radius=12)

            # Bouton Continuer
            continue_rect_area = pygame.Rect(pause_rect.x + 50, pause_rect.y + 30, 400, 50)
            continue_color = (255,255,0) if continue_rect_area.collidepoint(mouse_pos) else (255,255,255)
            continue_text = pause_font.render("Continuer", True, continue_color)
            continue_rect = continue_text.get_rect(center=(pause_rect.centerx, pause_rect.y + 55))
            screen.blit(continue_text, continue_rect)

            # Bouton Quitter
            quit_rect_area = pygame.Rect(pause_rect.x + 50, pause_rect.y + 110, 400, 50)
            quit_color = (255,255,0) if quit_rect_area.collidepoint(mouse_pos) else (255,255,255)
            quit_text_pause = pause_font.render("Quitter", True, quit_color)
            quit_rect_pause = quit_text_pause.get_rect(center=(pause_rect.centerx, pause_rect.y + 135))
            screen.blit(quit_text_pause, quit_rect_pause)

    # Menu principal ou fin de partie
    else:
        if not game.is_game_over:
            screen.blit(banner, banner_rect)

            if play_button_rect.collidepoint(mouse_pos):
                screen.blit(play_button_hover, play_button_hover_rect)
            else:
                screen.blit(play_button, play_button_rect)

            if credits_rect.collidepoint(mouse_pos):
                screen.blit(credits_img_hover, credits_hover_rect)
            else:
                screen.blit(credits_img, credits_rect)

            if quit_rect.collidepoint(mouse_pos):
                screen.blit(quit_img_hover, quit_hover_rect)
            else:
                screen.blit(quit_img, quit_rect)

        else:
            # Fin de partie
            game_over_img = pygame.image.load("Projet jeux python en 2D/assets/Game_over.png").convert_alpha()
            game_over_img = pygame.transform.scale(game_over_img, (1920,1080))
            screen.blit(game_over_img,(0,0))

            title = title_font.render("Vous avez péri", True,(255,0,0))
            screen.blit(title,title.get_rect(center=(screen.get_width()//2,int(screen.get_height()*0.11))))

            if restart_rect.collidepoint(mouse_pos):
                color = (255,255,0)
                hover_font = pygame.font.Font("Projet jeux python en 2D/assets/CustomFont.ttf",40)
                text = hover_font.render("Recommencer une nouvelle partie", True,color)
            else:
                text = text_font.render("Recommencer une nouvelle partie", True,(255,255,255))
            screen.blit(text,text.get_rect(center=restart_rect.center))

            if menu_rect.collidepoint(mouse_pos):
                hover_font = pygame.font.Font("Projet jeux python en 2D/assets/CustomFont.ttf",40)
                text = hover_font.render("Retour au menu principale", True,(255,255,0))
            else:
                text = text_font.render("Retour au menu principale", True,(255,255,255))
            screen.blit(text,text.get_rect(center=menu_rect.center))

    # Popup crédits
    if show_popup:
        overlay = pygame.Surface((1920,1080),pygame.SRCALPHA)
        overlay.fill((0,0,0,150))
        screen.blit(overlay,(0,0))

        popup_rect = pygame.Rect((screen.get_width() - popup_width)//2,
                                 (screen.get_height() - popup_height)//2,
                                 popup_width,
                                 popup_height)
        close_btn_center = (popup_rect.right - 30, popup_rect.top + 30)

        pygame.draw.rect(screen,(240,240,240),popup_rect,border_radius=12)
        pygame.draw.rect(screen,(0,0,0),popup_rect,width=3,border_radius=12)

        text1 = credit_font.render("Jeu créé et développé par",True,(0,0,0))
        text2 = credit_font.render("Aurélien Wins",True,(0,0,0))
        text1_rect = text1.get_rect(center=(popup_rect.centerx,popup_rect.top + popup_rect.height*0.35))
        text2_rect = text2.get_rect(center=(popup_rect.centerx,popup_rect.top + popup_rect.height*0.55))
        screen.blit(text1,text1_rect)
        screen.blit(text2,text2_rect)

        pygame.draw.circle(screen,(200,0,0),close_btn_center,close_btn_radius)
        pygame.draw.line(screen,(255,255,255),(close_btn_center[0]-8,close_btn_center[1]-8),(close_btn_center[0]+8,close_btn_center[1]+8),3)
        pygame.draw.line(screen,(255,255,255),(close_btn_center[0]+8,close_btn_center[1]-8),(close_btn_center[0]-8,close_btn_center[1]+8),3)

    pygame.display.flip()

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Le jeu se ferme")

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game.is_playing and not is_paused:
                game.player.launch_projectile()
            elif event.key == pygame.K_ESCAPE and game.is_playing:
                is_paused = not is_paused
            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx,my = event.pos

            # Fermer popup
            if show_popup and math.hypot(mx - close_btn_center[0], my - close_btn_center[1]) <= close_btn_radius:
                show_popup = False
                continue

            # Menu pause
            if is_paused:
                if continue_rect.collidepoint((mx,my)):
                    is_paused = False
                elif quit_rect_pause.collidepoint((mx,my)):
                    is_paused = False
                    game.is_playing = False
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("Projet jeux python en 2D/assets/sounds/musique_ecran_d'acceuil.ogg")
                    pygame.mixer.music.play(-1,fade_ms=50)
                continue

            # Menu principal
            if not game.is_playing and not game.is_game_over:
                if play_button_rect.collidepoint(event.pos):
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(game_music_path)
                    pygame.mixer.music.play(-1,fade_ms=50)
                    game.start()
                    game.sound_manager.play("click")
                    manche_start_time = pygame.time.get_ticks()
                elif credits_rect.collidepoint(event.pos):
                    show_popup = True
                    game.sound_manager.play("click")
                elif quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

            # Fin de partie
            if game.is_game_over:
                if restart_rect.collidepoint(event.pos):
                    game.is_game_over = False
                    game.start()
                    manche_start_time = pygame.time.get_ticks()
                    game.sound_manager.play("click")
                elif menu_rect.collidepoint(event.pos):
                    game.is_game_over = False
                    game.is_playing = False
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("Projet jeux python en 2D/assets/sounds/musique_ecran_d'acceuil.ogg")
                    pygame.mixer.music.play(-1,fade_ms=50)
                    game.sound_manager.play("click")

    clock.tick(FPS)


























