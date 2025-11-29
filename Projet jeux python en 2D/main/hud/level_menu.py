import pygame
from ..configuration import *

# Les différentes polices d'écriture utilisées dans le menu
title_font = pygame.font.Font(FONT_PATH, TITLE_FONT_SIZE)
text_font = pygame.font.Font(FONT_PATH, TEXT_FONT_SIZE)

class LevelMenu:
    # Classe pour gérer le menu de sélection des niveaux
    def __init__(self, screen, level_scores):
        self.screen = screen
        self.level_scores = level_scores

        # Charger les images du menu
        # J'ai utilisé smoothscale pour éviter les pixels
        self.background = pygame.image.load(BACKGROUND_PATH).convert()
        self.background = pygame.transform.smoothscale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.banner = pygame.image.load(BANNER_PATH).convert_alpha()
        self.banner = pygame.transform.scale(self.banner, (int(SCREEN_WIDTH * BANNER_SCALE_FACTOR), int(SCREEN_HEIGHT * BANNER_HEIGHT_FACTOR)))
        self.banner_rect = self.banner.get_rect()
        self.banner_rect.centerx = SCREEN_WIDTH // 2
        self.banner_rect.y = int(SCREEN_HEIGHT * BANNER_Y_FACTOR)

        # Titre du menu des différents niveaux de jeu
        self.title_text = title_font.render("Voici les différent niveaux a completer", True, BLACK)
        self.title_rect = self.title_text.get_rect()
        self.title_rect.centerx = SCREEN_WIDTH // 6

        self.level_rects = []
        self.level_colors = [(70, 130, 180), (60, 179, 113), (255, 69, 0)]  
        self.level_hover_colors = [(100, 160, 210), (90, 209, 143), (255, 99, 30)]
        self.shadow_color = (0, 0, 0, 100)  

        # Images a mettre a gauche des du texte (a changer dans le futur)
        self.level_images = [
            pygame.transform.scale(pygame.image.load(OGRE_IMG_PATH).convert_alpha(), (80, 80)),
            pygame.transform.scale(pygame.image.load(DRAGON_IMG_PATH).convert_alpha(), (80, 80)),
            pygame.transform.scale(pygame.image.load(COMET_IMG_PATH).convert_alpha(), (80, 80))
        ]

        card_width = 400
        card_height = 120
        spacing = 10
        button_height = 60

        # mise a l'échelle du menu 
        title_height = self.title_rect.height
        total_height = title_height + 3 * card_height + 2 * spacing + button_height + 20
        start_y = (SCREEN_HEIGHT - total_height) // 2  

        self.title_rect.y = start_y
        current_y = self.title_rect.bottom + 10

        for i in range(1, 4):
            rect = pygame.Rect(0, 0, card_width, card_height)
            rect.centerx = SCREEN_WIDTH // 6  
            rect.y = current_y
            self.level_rects.append(rect)
            current_y += card_height + spacing

        # Bouton retour uniquement dans le menu niveaux
        self.back_button = pygame.image.load(RETOUR_IMG_PATH).convert_alpha()
        button_width = 500
        button_height = 150
        self.back_button = pygame.transform.scale(self.back_button, (button_width, button_height))
        self.back_button_rect = self.back_button.get_rect()
        self.back_button_rect.centerx = SCREEN_WIDTH // 6
        self.back_button_rect.y = current_y
        self.back_button_hover = pygame.transform.scale(self.back_button, (int(button_width * 1.05), int(button_height * 1.05)))
        self.back_button_hover_rect = self.back_button_hover.get_rect(center=self.back_button_rect.center)

    # Cette méthode de dessin est assez longue (il faudrait trouver un moyen de la réduire)
    def draw(self, mouse_pos, overlay=False):
        if not overlay:
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.banner, self.banner_rect)
        if overlay:
            center_offset = SCREEN_WIDTH // 2 - SCREEN_WIDTH // 6
            title_rect = self.title_text.get_rect(centerx=self.title_rect.centerx + center_offset, y=self.title_rect.y)
            self.screen.blit(self.title_text, title_rect)
        else:
            self.screen.blit(self.title_text, self.title_rect)

        center_offset = (SCREEN_WIDTH // 2 - SCREEN_WIDTH // 6) if overlay else 0
        # Dessiner chaque niveau
        for i in range(3):
            rect = self.level_rects[i]
            adjusted_rect = rect.move(center_offset, 0)
            # Seuils pour débloquer les niveaux
            thresholds = {1: 0, 2: 500, 3: 500}  # Niveau 1 toujours débloqué, 2 si score niv1 >=500, 3 si score niv2 >=500
            prev_level = i  # Pour niveau 1, pas de précédent, pour 2, niv1, pour 3, niv2
            required_score = self.level_scores.get(prev_level, 0) if i > 0 else 0
            is_locked = required_score < thresholds[i+1]
            is_hover = adjusted_rect.collidepoint(mouse_pos) and not is_locked
            color = self.level_hover_colors[i] if is_hover else self.level_colors[i]
            if is_locked:
                color = (169, 169, 169)  # La couleur grise pour verrouillé le niveaux

            # Une ombre pour l'effet 3D
            shadow_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
            pygame.draw.rect(shadow_surface, self.shadow_color, (0, 0, rect.width, rect.height), border_radius=10)
            self.screen.blit(shadow_surface, (adjusted_rect.x + 5, adjusted_rect.y + 5))

            pygame.draw.rect(self.screen, color, adjusted_rect, border_radius=10)
            pygame.draw.rect(self.screen, BLACK, adjusted_rect, 2, border_radius=10)

            # Ce bloc rajoute les effet de survol
            if is_hover:
                glow_color = (255, 255, 255, 50) 
                glow_surface = pygame.Surface((rect.width + 10, rect.height + 10), pygame.SRCALPHA)
                pygame.draw.rect(glow_surface, glow_color, (0, 0, rect.width + 10, rect.height + 10), border_radius=15)
                self.screen.blit(glow_surface, (adjusted_rect.x - 5, adjusted_rect.y - 5))
                # Cela permet de creer le petit cadeans quand le niveaux n'est pas débloquer pour retirer l'accès au joueur
            if is_locked:
                lock_center = (adjusted_rect.left + 60, adjusted_rect.centery)
                pygame.draw.rect(self.screen, (0, 0, 0), (lock_center[0] - 15, lock_center[1] - 10, 30, 20), border_radius=5)
                pygame.draw.arc(self.screen, (0, 0, 0), (lock_center[0] - 10, lock_center[1] - 20, 20, 20), 0, 3.14, 3)
                pygame.draw.circle(self.screen, (255, 255, 255), lock_center, 3)
                pygame.draw.rect(self.screen, (255, 255, 255), (lock_center[0] - 1, lock_center[1], 2, 8))
            else:
                scale_factor = 1.1 if is_hover else 1.0
                img_size = int(80 * scale_factor)
                scaled_img = pygame.transform.scale(self.level_images[i], (img_size, img_size))
                img_rect = scaled_img.get_rect(center=(adjusted_rect.left + 60, adjusted_rect.centery))
                self.screen.blit(scaled_img, img_rect)

            level_text = text_font.render(f"Niveau {i+1}", True, BLACK)
            text_rect = level_text.get_rect(center=(adjusted_rect.centerx + 40, adjusted_rect.centery - 10))
            self.screen.blit(level_text, text_rect)

            score_text = text_font.render(f"Meilleur: {self.level_scores.get(i+1, 0)}", True, BLACK)
            score_rect = score_text.get_rect(center=(adjusted_rect.centerx + 40, adjusted_rect.centery + 10))
            self.screen.blit(score_text, score_rect)

        # Bouton retour gestion de colission et gestion de l'emplacement sur la fenetre de jeux
        adjusted_back_rect = self.back_button_rect.move(center_offset, 0)
        adjusted_back_hover_rect = self.back_button_hover_rect.move(center_offset, 0)
        if adjusted_back_rect.collidepoint(mouse_pos):
            self.screen.blit(self.back_button_hover, adjusted_back_hover_rect)
        else:
            self.screen.blit(self.back_button, adjusted_back_rect)

    def handle_click(self, pos, overlay=False):
        center_offset = (SCREEN_WIDTH // 2 - SCREEN_WIDTH // 6) if overlay else 0
        for i in range(3):
            thresholds = {1: 0, 2: 500, 3: 500}
            prev_level = i
            required_score = self.level_scores.get(prev_level, 0) if i > 0 else 0
            if required_score >= thresholds[i+1]:
                adjusted_rect = self.level_rects[i].move(center_offset, 0)
                if adjusted_rect.collidepoint(pos):
                    return f"level_{i+1}"
        adjusted_back_rect = self.back_button_rect.move(center_offset, 0)
        if adjusted_back_rect.collidepoint(pos):
            return "back"
        return None