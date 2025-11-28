import pygame
from ..configuration import *

# Les différentes polices d'écriture utilisées dans le menu
title_font = pygame.font.Font(FONT_PATH, TITLE_FONT_SIZE)
text_font = pygame.font.Font(FONT_PATH, TEXT_FONT_SIZE)

class LevelMenu:
    def __init__(self, screen):
        self.screen = screen

        # Charger les images du menu
        self.background = pygame.image.load(BACKGROUND_PATH).convert()
        self.background = pygame.transform.smoothscale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.banner = pygame.image.load(BANNER_PATH).convert_alpha()
        self.banner = pygame.transform.scale(self.banner, (int(SCREEN_WIDTH * BANNER_SCALE_FACTOR), int(SCREEN_HEIGHT * BANNER_HEIGHT_FACTOR)))
        self.banner_rect = self.banner.get_rect()
        self.banner_rect.centerx = SCREEN_WIDTH // 2
        self.banner_rect.y = int(SCREEN_HEIGHT * BANNER_Y_FACTOR)

        # Titre du menu niveaux
        self.title_text = title_font.render("Voici les niveaux", True, BLACK)
        self.title_rect = self.title_text.get_rect()
        self.title_rect.centerx = SCREEN_WIDTH // 2

        self.level_rects = []
        self.level_colors = [(100, 200, 100), (200, 200, 100), (200, 100, 100)] 
        self.level_hover_colors = [(150, 250, 150), (250, 250, 150), (250, 150, 150)]

        # Images pour les niveaux
        self.level_images = [
            pygame.transform.scale(pygame.image.load(OGRE_IMG_PATH).convert_alpha(), (50, 50)),
            pygame.transform.scale(pygame.image.load(DRAGON_IMG_PATH).convert_alpha(), (50, 50)),
            pygame.transform.scale(pygame.image.load(COMET_IMG_PATH).convert_alpha(), (50, 50))
        ]

        card_width = 300
        card_height = 80
        spacing = 10
        button_height = 35

        # mise a l'échelle
        title_height = self.title_rect.height
        total_height = title_height + 3 * card_height + 2 * spacing + button_height + 20  
        start_y = (SCREEN_HEIGHT - total_height) // 2 + self.banner_rect.bottom // 2  

        self.title_rect.y = start_y
        current_y = self.title_rect.bottom + 10

        for i in range(1, 4):
            rect = pygame.Rect(0, 0, card_width, card_height)
            rect.centerx = SCREEN_WIDTH // 2
            rect.y = current_y
            self.level_rects.append(rect)
            current_y += card_height + spacing

        # Bouton retour
        self.back_button = pygame.image.load(BUTTON_PATH).convert_alpha()
        self.back_button = pygame.transform.scale(self.back_button, (int(SCREEN_WIDTH * BUTTON_SCALE_FACTOR), button_height))
        self.back_button_rect = self.back_button.get_rect()
        self.back_button_rect.centerx = SCREEN_WIDTH // 2
        self.back_button_rect.y = current_y
        self.back_button_hover = pygame.transform.scale(self.back_button, (int(SCREEN_WIDTH * 0.27), 42))
        self.back_button_hover_rect = self.back_button_hover.get_rect(center=self.back_button_rect.center)

    def draw(self, mouse_pos):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.banner, self.banner_rect)
        self.screen.blit(self.title_text, self.title_rect)

        for i in range(3):
            color = self.level_hover_colors[i] if self.level_rects[i].collidepoint(mouse_pos) else self.level_colors[i]
            pygame.draw.rect(self.screen, color, self.level_rects[i], border_radius=10)
            pygame.draw.rect(self.screen, BLACK, self.level_rects[i], 2, border_radius=10) 

            # Image du niveau
            img_rect = self.level_images[i].get_rect(center=(self.level_rects[i].left + 40, self.level_rects[i].centery))
            self.screen.blit(self.level_images[i], img_rect)

            # Texte du niveau
            level_text = text_font.render(f"Niveau {i+1}", True, BLACK)
            text_rect = level_text.get_rect(center=(self.level_rects[i].centerx + 30, self.level_rects[i].centery))
            self.screen.blit(level_text, text_rect)

        # Bouton retour
        if self.back_button_rect.collidepoint(mouse_pos):
            self.screen.blit(self.back_button_hover, self.back_button_hover_rect)
        else:
            self.screen.blit(self.back_button, self.back_button_rect)

        back_text = text_font.render("Retour", True, BLACK)
        back_text_rect = back_text.get_rect(center=self.back_button_rect.center)
        self.screen.blit(back_text, back_text_rect)

    def handle_click(self, pos):
        for i in range(3):
            if self.level_rects[i].collidepoint(pos):
                return f"level_{i+1}"
        if self.back_button_rect.collidepoint(pos):
            return "back"
        return None