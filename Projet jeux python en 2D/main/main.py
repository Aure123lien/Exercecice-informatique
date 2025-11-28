import pygame
import sys
import math
pygame.init()

from .game import Game
from .hud.menu import MainMenu
from .hud.level_menu import LevelMenu
from .hud.settings import SettingsMenu
from .hud.game_over import GameOverScreen
from .hud.pause import PauseMenu
from .hud.credits import CreditsPopup
from .configuration import *

# Différentes polices d'écriture utilisées dans le jeu
# J'ai mis ça en global parce que c'est plus simple pour l'instant
title_font = pygame.font.Font(FONT_PATH, TITLE_FONT_SIZE)
text_font = pygame.font.Font(FONT_PATH, TEXT_FONT_SIZE)
credit_font = pygame.font.Font(FONT_PATH, CREDIT_FONT_SIZE)
pause_font = pygame.font.Font(FONT_PATH, PAUSE_FONT_SIZE)
font_small = pygame.font.Font(None, SMALL_FONT_SIZE)

# Musique du menu
pygame.mixer.music.load(MUSIC_MENU_PATH)
pygame.mixer.music.set_volume(INITIAL_MUSIC_VOLUME)
pygame.mixer.music.play(-1, fade_ms=50)

# Le timer dans le jeu
clock = pygame.time.Clock()

# Musique du jeu
game_music_path = MUSIC_GAME_PATH

# Menu pause
is_paused = False

# Je vais creer une classe setting plus tard 
# Fonction pour changer le mode écran
def set_screen_mode(mode):
    global screen, SCREEN_WIDTH, SCREEN_HEIGHT, background, bg_width, bg_height, scale, new_width, new_height, bg_x, bg_y
    # Dimensions pour le mode fenêtre plein écran
    # J'ai choisi 1920x1080 parce que c'est une résolution commune a la plus part des ordinateur
    windowed_width = 1920
    windowed_height = 1080

    if mode == 0:  # Fenêtré plein écran
        screen = pygame.display.set_mode((windowed_width, windowed_height), pygame.NOFRAME)
        SCREEN_WIDTH, SCREEN_HEIGHT = windowed_width, windowed_height
    elif mode == 1:  # Plein écran
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()

    # Recalculer le l'affichage du fond d'ecran
    background = pygame.image.load(BACKGROUND_PATH).convert()
    bg_width, bg_height = background.get_size()
    scale_x = SCREEN_WIDTH / bg_width
    scale_y = SCREEN_HEIGHT / bg_height
    scale = min(scale_x, scale_y)
    new_width = int(bg_width * scale)
    new_height = int(bg_height * scale)
    background = pygame.transform.smoothscale(background, (new_width, new_height))
    bg_x = (SCREEN_WIDTH - new_width) // 2
    bg_y = (SCREEN_HEIGHT - new_height) // 2

# Sa prend la resolution du bureau
pygame.display.set_caption("Jeu de tir en 2D")
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()

# Charger le jeu
game = Game()
manche_start_time = 0

# Fond d'écran du jeu
background = pygame.image.load(BACKGROUND_PATH).convert()
bg_width, bg_height = background.get_size()
scale_x = SCREEN_WIDTH / bg_width
scale_y = SCREEN_HEIGHT / bg_height
scale = min(scale_x, scale_y)
new_width = int(bg_width * scale)
new_height = int(bg_height * scale)
background = pygame.transform.smoothscale(background, (new_width, new_height))
bg_x = (SCREEN_WIDTH - new_width) // 2
bg_y = (SCREEN_HEIGHT - new_height) // 2

# Volume 
music_volume = INITIAL_MUSIC_VOLUME
sound_volume = INITIAL_SOUND_VOLUME
pygame.mixer.music.set_volume(music_volume)
game.sound_manager.set_volume(sound_volume)

# Toutes les interface afficher
main_menu = MainMenu(screen, game.best_score)
level_menu = LevelMenu(screen, game.level_scores)
settings_menu = SettingsMenu(screen)
game_over_screen = GameOverScreen(screen)
pause_menu = PauseMenu(screen)
credits_popup = CreditsPopup(screen)

# Les variables des menus
show_settings = False
show_popup = False
show_level_menu = False

# Amélioration s'est de splitter cette boucle en différente fonction
# Début de la boucle principale du jeux
running = True
while running:
    if game.is_playing:
        screen.blit(background, (bg_x, bg_y))
    mouse_pos = pygame.mouse.get_pos()

    # Gestion de l'affichage pendant le jeu
    # Quand la partie est en cours
    if game.is_playing:

        if not is_paused:
            game.update(screen)
            score_text = text_font.render(f"Score : {game.player.score}", True, WHITE)
            screen.blit(score_text, score_text.get_rect(center=(SCREEN_WIDTH//2, int(SCREEN_HEIGHT * 0.05))))
            elapsed_time = (pygame.time.get_ticks() - manche_start_time)//1000
            timer_text = text_font.render(f"Temps : {elapsed_time}s", True, WHITE)
            screen.blit(timer_text, timer_text.get_rect(topleft=(int(SCREEN_WIDTH * 0.02), int(SCREEN_HEIGHT * 0.02))))
        else:
            continue_rect, settings_rect_area, quit_rect_area = pause_menu.draw(mouse_pos)
            if show_settings:
                close_btn = settings_menu.draw()

    # Menu principal et de fin
    else:
        if show_level_menu:
            main_menu.best_score = game.best_score
            level_menu.level_scores = game.level_scores
            main_menu.draw(mouse_pos, no_banner=True, hide_buttons=True)
            level_menu.draw(mouse_pos, overlay=True)
        elif not game.is_game_over:
            main_menu.best_score = game.best_score
            main_menu.draw(mouse_pos)
        else:
            game_over_screen.draw(mouse_pos)

    # La popup crédit
    if show_popup:
        credits_popup.draw()

    if show_settings and not game.is_playing:
        close_btn = settings_menu.draw()

    pygame.display.flip()

    # Gestion des événements mal optimiser (a revoir)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.save_level_scores()
            game.save_best_score()
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
            mx, my = event.pos
            if show_settings and settings_menu.music_slider_rect.collidepoint(event.pos):
                settings_menu.dragging_music = True
            if show_settings and settings_menu.sound_slider_rect.collidepoint(event.pos):
                settings_menu.dragging_sound = True
            # Gérer les changements de mode écran
            if show_settings:
                old_mode = settings_menu.get_fullscreen_mode()
                settings_menu.handle_mouse_down(event.pos)
                new_mode = settings_menu.get_fullscreen_mode()
                if old_mode != new_mode:
                    set_screen_mode(new_mode)
                    game.sound_manager.play("click")
            # Fermer la fenêtre réglages
            if show_settings and close_btn.collidepoint(event.pos):
                show_settings = False
            # Menu pause
            if is_paused:
                if continue_rect.collidepoint((mx, my)):
                    is_paused = False
                elif settings_rect_area.collidepoint((mx, my)):
                    show_settings = True
                elif quit_rect_area.collidepoint((mx, my)):
                    is_paused = False
                    game.is_playing = False
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(MUSIC_MENU_PATH)
                    pygame.mixer.music.play(-1, fade_ms=50)
            # Ouvrir menu réglages depuis menu principal
            if not game.is_playing and not game.is_game_over and not show_level_menu:
                action = main_menu.handle_click(event.pos)
                if action == "settings":
                    show_settings = True
                elif action == "play":
                    show_level_menu = True
                    game.sound_manager.play("click")
                elif action == "credits":
                    show_popup = True
                    game.sound_manager.play("click")
                elif action == "quit":
                    pygame.quit()
                    sys.exit()
            # Gestion du menu de niveaux
            elif show_level_menu:
                action = level_menu.handle_click(event.pos, overlay=True)
                if action == "back":
                    show_level_menu = False
                    game.sound_manager.play("click")
                elif action and action.startswith("level_"):
                    level = int(action.split("_")[1])
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(game_music_path)
                    pygame.mixer.music.play(-1, fade_ms=50)
                    game.start(level=level)
                    game.sound_manager.play("click")
                    manche_start_time = pygame.time.get_ticks()
                    show_level_menu = False
            # Fermer popup crédits
            if show_popup and credits_popup.handle_click(event.pos) == "close":
                show_popup = False
            # Fin partie
            if game.is_game_over:
                action = game_over_screen.handle_click(event.pos)
                if action == "restart":
                    game.is_game_over = False
                    game.start()
                    manche_start_time = pygame.time.get_ticks()
                    game.sound_manager.play("click")
                elif action == "menu":
                    game.is_game_over = False
                    game.is_playing = False
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(MUSIC_MENU_PATH)
                    pygame.mixer.music.play(-1, fade_ms=50)
                    game.sound_manager.play("click")
        elif event.type == pygame.MOUSEBUTTONUP:
            settings_menu.handle_mouse_up()
        elif event.type == pygame.MOUSEMOTION:
            settings_menu.handle_mouse_motion(event)
            music_volume, sound_volume = settings_menu.get_volumes()
            pygame.mixer.music.set_volume(music_volume)
            game.sound_manager.set_volume(sound_volume)
            if settings_menu.dragging_sound:
                game.sound_manager.play("click")

    clock.tick(FPS)