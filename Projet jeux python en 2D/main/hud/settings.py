import pygame
import json
import os
from ..configuration import *

font_small = pygame.font.Font(None, SMALL_FONT_SIZE)

class SettingsMenu:
    def __init__(self, screen):
        self.screen = screen
        self.settings_file = os.path.join(os.path.dirname(__file__), '..', '..', 'settings.json')
        self.music_volume = INITIAL_MUSIC_VOLUME
        self.sound_volume = INITIAL_SOUND_VOLUME
        self.fullscreen_mode = 0  # 0: fenetre pleine ecran, 1: Pleine ecran
        self.load_settings()

        # Les barres de volume du son et musiques
        self.music_bar_rect = pygame.Rect(0, 0, 200, 10)
        self.music_slider_rect = pygame.Rect(0, 0, 20, 20)
        self.sound_bar_rect = pygame.Rect(0, 0, 200, 10)
        self.sound_slider_rect = pygame.Rect(0, 0, 20, 20)
        self.dragging_music = False
        self.dragging_sound = False

        # Boutons pour le mode écran
        self.windowed_fullscreen_btn_rect = pygame.Rect(0, 0, 150, 40)
        self.fullscreen_btn_rect = pygame.Rect(0, 0, 150, 40)

        # Les polices d'écriture
        self.font_small = pygame.font.Font(None, SMALL_FONT_SIZE)

    def load_settings(self):
        if os.path.exists(self.settings_file):
            try:
                with open(self.settings_file, 'r') as f:
                    data = json.load(f)
                    self.music_volume = data.get('music_volume', INITIAL_MUSIC_VOLUME)
                    self.sound_volume = data.get('sound_volume', INITIAL_SOUND_VOLUME)
                    self.fullscreen_mode = data.get('fullscreen_mode', 0)
            except (json.JSONDecodeError, KeyError):
                pass  # Utiliser les valeurs par défaut en cas d'erreur

    def save_settings(self):
        data = {
            'music_volume': self.music_volume,
            'sound_volume': self.sound_volume,
            'fullscreen_mode': self.fullscreen_mode
        }
        try:
            with open(self.settings_file, 'w') as f:
                json.dump(data, f, indent=4)
        except IOError:
            pass  # Ignorer les erreurs d'écriture

    def draw(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        self.screen.blit(overlay, (0, 0))

        settings_window = pygame.Rect(
            (SCREEN_WIDTH - SETTINGS_WINDOW_WIDTH) // 2,
            (SCREEN_HEIGHT - SETTINGS_WINDOW_HEIGHT) // 2,
            SETTINGS_WINDOW_WIDTH,
            SETTINGS_WINDOW_HEIGHT
        )
        pygame.draw.rect(self.screen, DARK_GRAY, settings_window, border_radius=12)
        pygame.draw.rect(self.screen, WHITE, settings_window, 3, border_radius=12)

        margin_x = MUSIC_BAR_MARGIN_X
        music_bar_y = settings_window.top + MUSIC_BAR_Y
        sound_bar_y = settings_window.top + SOUND_BAR_Y

        # Barre de musique
        self.music_bar_rect.topleft = (settings_window.left + margin_x, music_bar_y)
        self.music_bar_rect.width = settings_window.width - 2 * margin_x
        self.music_slider_rect.y = self.music_bar_rect.y - 5
        self.music_slider_rect.x = self.music_bar_rect.x + self.music_volume * self.music_bar_rect.width - 10
        pygame.draw.rect(self.screen, LIGHT_GRAY, self.music_bar_rect)
        pygame.draw.rect(self.screen, YELLOW, self.music_slider_rect)
        self.screen.blit(self.font_small.render("Musique", True, WHITE), (self.music_bar_rect.x, self.music_bar_rect.y - 30))

        # Barre de sons
        self.sound_bar_rect.topleft = (settings_window.left + margin_x, sound_bar_y)
        self.sound_bar_rect.width = settings_window.width - 2 * margin_x
        self.sound_slider_rect.y = self.sound_bar_rect.y - 5
        self.sound_slider_rect.x = self.sound_bar_rect.x + self.sound_volume * self.sound_bar_rect.width - 10
        pygame.draw.rect(self.screen, LIGHT_GRAY, self.sound_bar_rect)
        pygame.draw.rect(self.screen, YELLOW, self.sound_slider_rect)
        self.screen.blit(self.font_small.render("Sons", True, WHITE), (self.sound_bar_rect.x, self.sound_bar_rect.y - 30))

        # Boutons pour le mode écran
        fullscreen_y = sound_bar_y + 60
        self.windowed_fullscreen_btn_rect.topleft = (settings_window.left + margin_x, fullscreen_y)
        self.fullscreen_btn_rect.topleft = (settings_window.left + margin_x + 170, fullscreen_y)

        # Bouton Fenêtre plein écran
        color_windowed_fs = GREEN if self.fullscreen_mode == 0 else GRAY
        pygame.draw.rect(self.screen, color_windowed_fs, self.windowed_fullscreen_btn_rect, border_radius=5)
        pygame.draw.rect(self.screen, WHITE, self.windowed_fullscreen_btn_rect, 2, border_radius=5)
        windowed_fs_text = self.font_small.render("Fen. P. Écran", True, WHITE)
        self.screen.blit(windowed_fs_text, windowed_fs_text.get_rect(center=self.windowed_fullscreen_btn_rect.center))

        # Bouton Plein écran
        color_fullscreen = GREEN if self.fullscreen_mode == 1 else GRAY
        pygame.draw.rect(self.screen, color_fullscreen, self.fullscreen_btn_rect, border_radius=5)
        pygame.draw.rect(self.screen, WHITE, self.fullscreen_btn_rect, 2, border_radius=5)
        fullscreen_text = self.font_small.render("Plein écran", True, WHITE)
        self.screen.blit(fullscreen_text, fullscreen_text.get_rect(center=self.fullscreen_btn_rect.center))

        # Bouton de fermeture de la fenetre
        close_btn = pygame.Rect(settings_window.right - 40, settings_window.top + 10, 30, 30)
        pygame.draw.rect(self.screen, RED, close_btn)
        pygame.draw.line(self.screen, WHITE, (close_btn.left + 5, close_btn.top + 5), (close_btn.right - 5, close_btn.bottom - 5), 3)
        pygame.draw.line(self.screen, WHITE, (close_btn.right - 5, close_btn.top + 5), (close_btn.left + 5, close_btn.bottom - 5), 3)

        return close_btn

    def handle_mouse_motion(self, event):
        if self.dragging_music:
            rel_x = max(0, min(event.pos[0] - self.music_bar_rect.x, self.music_bar_rect.width))
            self.music_volume = rel_x / self.music_bar_rect.width
            self.music_slider_rect.x = self.music_bar_rect.x + rel_x - 10
            self.save_settings()
        if self.dragging_sound:
            rel_x = max(0, min(event.pos[0] - self.sound_bar_rect.x, self.sound_bar_rect.width))
            self.sound_volume = rel_x / self.sound_bar_rect.width
            self.sound_slider_rect.x = self.sound_bar_rect.x + rel_x - 10
            self.save_settings()

    def handle_mouse_down(self, pos):
        if self.music_slider_rect.collidepoint(pos):
            self.dragging_music = True
        if self.sound_slider_rect.collidepoint(pos):
            self.dragging_sound = True
        if self.windowed_fullscreen_btn_rect.collidepoint(pos):
            self.fullscreen_mode = 0
            self.save_settings()
        if self.fullscreen_btn_rect.collidepoint(pos):
            self.fullscreen_mode = 1
            self.save_settings()

    def handle_mouse_up(self):
        self.dragging_music = False
        self.dragging_sound = False

    def get_volumes(self):
        return self.music_volume, self.sound_volume

    def get_fullscreen_mode(self):
        return self.fullscreen_mode