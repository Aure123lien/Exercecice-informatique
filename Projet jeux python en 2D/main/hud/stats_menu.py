import pygame
from ..configuration import *

# Les différentes polices d'écriture utilisées dans le menu
title_font = pygame.font.Font(FONT_PATH, TITLE_FONT_SIZE)
text_font = pygame.font.Font(FONT_PATH, TEXT_FONT_SIZE)

class StatsMenu:
    def __init__(self, screen, player, best_score, level_scores):
        self.screen = screen
        self.player = player
        self.best_score = best_score
        self.level_scores = level_scores

        # Charger les images du menu
        self.background = pygame.image.load(BACKGROUND_PATH).convert()
        self.background = pygame.transform.smoothscale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Titre
        self.title_text = title_font.render("Statistiques du Personnage", True, BLACK)
        self.title_rect = self.title_text.get_rect()
        self.title_rect.centerx = SCREEN_WIDTH // 2
        self.title_rect.y = SCREEN_HEIGHT // 2 - 150 

        # Bouton retour
        self.back_button = pygame.image.load(RETOUR_IMG_PATH).convert_alpha()
        self.back_button = pygame.transform.scale(self.back_button, (200, 100))
        self.back_button_rect = self.back_button.get_rect()
        self.back_button_rect.centerx = SCREEN_WIDTH // 2
        self.back_button_rect.y = SCREEN_HEIGHT - 150
        self.back_button_hover = pygame.transform.scale(self.back_button, (int(200 * 1.05), int(100 * 1.05)))
        self.back_button_hover_rect = self.back_button_hover.get_rect(center=self.back_button_rect.center)

    def draw(self, mouse_pos):
        self.screen.blit(self.background, (0, 0))
        # Centrer le titre au milieu de l'écran
        self.screen.blit(self.title_text, self.title_rect)
        # Afficher les stats centrées
        y_offset = self.title_rect.bottom + 40
        stats = [
            f"Niveau: {self.player.level}",
            f"XP: {self.player.xp}/{self.player.xp_to_next}",
            f"Vie maximale: {self.player.max_health}",
            f"Attaque: {self.player.attack}",
            f"Vitesse: {self.player.velocity}"
        ]

        for stat in stats:
            text = text_font.render(stat, True, BLACK)
            rect = text.get_rect(centerx=SCREEN_WIDTH // 2, y=y_offset)
            self.screen.blit(text, rect)
            y_offset += 30

        # Bouton retour en bas
        if self.back_button_rect.collidepoint(mouse_pos):
            self.screen.blit(self.back_button_hover, self.back_button_hover_rect)
        else:
            self.screen.blit(self.back_button, self.back_button_rect)

    def handle_click(self, pos):
        if self.back_button_rect.collidepoint(pos):
            return "back"
        return None