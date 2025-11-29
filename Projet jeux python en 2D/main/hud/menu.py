import pygame
from ..configuration import *

# Les différentes polices d'écriture utilisées dans le menu
title_font = pygame.font.Font(FONT_PATH, TITLE_FONT_SIZE)
text_font = pygame.font.Font(FONT_PATH, TEXT_FONT_SIZE)

class MainMenu:
    def __init__(self, screen, best_score=0):
        self.screen = screen
        self.best_score = best_score

        # Charger les images du menu
        self.background = pygame.image.load(BACKGROUND_PATH).convert()
        self.background = pygame.transform.smoothscale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.banner = pygame.image.load(BANNER_PATH).convert_alpha()
        self.banner = pygame.transform.scale(self.banner, (int(SCREEN_WIDTH * BANNER_SCALE_FACTOR), int(SCREEN_HEIGHT * BANNER_HEIGHT_FACTOR)))
        self.banner_rect = self.banner.get_rect()
        self.banner_rect.centerx = SCREEN_WIDTH // 2
        self.banner_rect.y = int(SCREEN_HEIGHT * BANNER_Y_FACTOR)

        # Les différents boutons qui se trouvent dans le menu "jouer,credit,quitter"
        self.play_button = pygame.image.load(BUTTON_PATH).convert_alpha()
        self.play_button = pygame.transform.scale(self.play_button, (int(SCREEN_WIDTH * BUTTON_SCALE_FACTOR), int(SCREEN_HEIGHT * BUTTON_HEIGHT_FACTOR)))
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.centerx = SCREEN_WIDTH // 2
        self.play_button_rect.y = int(SCREEN_HEIGHT / BUTTON_Y_FACTOR)
        self.play_button_hover = pygame.transform.scale(self.play_button, (int(SCREEN_WIDTH * 0.27), int(SCREEN_HEIGHT * 0.15)))
        self.play_button_hover_rect = self.play_button_hover.get_rect(center=self.play_button_rect.center)

        self.credits_img_original = pygame.image.load(CREDITS_IMG_PATH).convert_alpha()
        self.credits_img = pygame.transform.scale(self.credits_img_original, (int(SCREEN_WIDTH * CREDITS_SCALE_FACTOR), int(SCREEN_HEIGHT * CREDITS_HEIGHT_FACTOR)))
        self.credits_rect = self.credits_img.get_rect(topright=(SCREEN_WIDTH - 20, 20))
        self.credits_img_hover = pygame.transform.scale(self.credits_img_original, (int(SCREEN_WIDTH * 0.135), int(SCREEN_HEIGHT * 0.08)))
        self.credits_hover_rect = self.credits_img_hover.get_rect(center=self.credits_rect.center)

        self.quit_img_original = pygame.image.load(QUIT_IMG_PATH).convert_alpha()
        self.quit_img = pygame.transform.scale(self.quit_img_original, (int(SCREEN_WIDTH * QUIT_SCALE_FACTOR), int(SCREEN_HEIGHT * QUIT_HEIGHT_FACTOR)))
        self.quit_rect = self.quit_img.get_rect()
        self.quit_rect.centerx = SCREEN_WIDTH // 2
        self.quit_rect.y = self.play_button_rect.y + self.play_button_rect.height + 20
        self.quit_img_hover = pygame.transform.scale(self.quit_img, (int(SCREEN_WIDTH * 0.27), int(SCREEN_HEIGHT * 0.15)))
        self.quit_hover_rect = self.quit_img_hover.get_rect(center=self.quit_rect.center)

        # Icône des paramètres
        self.settings_img_original = pygame.image.load(SETTINGS_IMG_PATH).convert_alpha()
        self.settings_img = pygame.transform.scale(self.settings_img_original, (int(SCREEN_WIDTH * SETTINGS_SCALE_FACTOR), int(SCREEN_HEIGHT * SETTINGS_HEIGHT_FACTOR)))
        self.settings_rect = self.settings_img.get_rect(bottomright=(SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20))
        self.settings_img_hover = pygame.transform.scale(self.settings_img_original, (int(SCREEN_WIDTH * 0.135), int(SCREEN_HEIGHT * 0.08)))
        self.settings_hover_rect = self.settings_img_hover.get_rect(center=self.settings_rect.center)

        # Bouton statistiques dans le menu
        self.stats_button = pygame.image.load(STATISTIQUE_IMG_PATH).convert_alpha()
        self.stats_button = pygame.transform.scale(self.stats_button, (int(SCREEN_WIDTH * BUTTON_SCALE_FACTOR), int(SCREEN_HEIGHT * BUTTON_HEIGHT_FACTOR)))
        self.stats_button_rect = self.stats_button.get_rect()
        self.stats_button_rect.bottomleft = (20, SCREEN_HEIGHT - 20)
        self.stats_button_hover = pygame.transform.scale(self.stats_button, (int(SCREEN_WIDTH * 0.27), int(SCREEN_HEIGHT * 0.15)))
        self.stats_button_hover_rect = self.stats_button_hover.get_rect(center=self.stats_button_rect.center)

    def draw(self, mouse_pos, no_banner=False, hide_buttons=False):
        self.screen.blit(self.background, (0, 0))
        if not no_banner:
            self.screen.blit(self.banner, self.banner_rect)
        if not hide_buttons:
            self.screen.blit(self.play_button_hover if self.play_button_rect.collidepoint(mouse_pos) else self.play_button, self.play_button_rect)

            self.screen.blit(self.credits_img_hover if self.credits_rect.collidepoint(mouse_pos) else self.credits_img, self.credits_rect)

            self.screen.blit(self.quit_img_hover if self.quit_rect.collidepoint(mouse_pos) else self.quit_img, self.quit_rect)

            self.screen.blit(self.stats_button_hover if self.stats_button_rect.collidepoint(mouse_pos) else self.stats_button, self.stats_button_rect)

            if self.settings_rect.collidepoint(mouse_pos):
                self.screen.blit(self.settings_img_hover, self.settings_hover_rect)
            else:
                self.screen.blit(self.settings_img, self.settings_rect)


    def handle_click(self, pos):
        if self.play_button_rect.collidepoint(pos):
            return "play"
        elif self.credits_rect.collidepoint(pos):
            return "credits"
        elif self.quit_rect.collidepoint(pos):
            return "quit"
        elif self.stats_button_rect.collidepoint(pos):
            return "stats"
        elif self.settings_rect.collidepoint(pos):
            return "settings"
        return None