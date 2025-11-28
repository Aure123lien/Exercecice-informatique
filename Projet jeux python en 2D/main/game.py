import pygame
import os
from .entitée.player import Player
from .entitée.monster import Dragon, Ogre
from .events.comet_event import CometFallEvent
from .audio.sound_manager import SoundManager
from .configuration import *

class Game:

    def __init__(self):
        self.is_playing = False
        self.is_game_over = False

        # Charger le meilleur score
        self.best_score_path = os.path.join(os.path.dirname(__file__), '..', 'best_score.txt')
        try:
            with open(self.best_score_path, 'r') as f:
                self.best_score = int(f.read().strip())
        except:
            self.best_score = 0

        # Joueur
        self.player = Player(self)
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player)

        # Événements
        self.comet_event = CometFallEvent(self)

        # Monstres
        self.all_monsters = pygame.sprite.Group()

        # Sons
        self.sound_manager = SoundManager()

        # Gestion des touches
        self.pressed = {}

        # affichage de la fin de la partie
        self.game_over_image = pygame.image.load(GAME_OVER_IMG_PATH).convert_alpha()
        self.game_over_image = pygame.transform.scale(self.game_over_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.go_title_font = pygame.font.Font(FONT_PATH, TITLE_FONT_SIZE)
        self.go_sub_font = pygame.font.Font(FONT_PATH, TEXT_FONT_SIZE)
        self.go_restart_button = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50, 300, 60)
        self.go_menu_button = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 30, 300, 60)

    # ajout des points pour les monstres
    def add_score(self, points):
        self.player.add_score(points)

    # Démarrer une partie
    def start(self, level=1):
        self.is_playing = True
        self.level = level
        self.player.rect.x = 350
        self.player.rect.y = SCREEN_HEIGHT - self.player.image.get_height() - 50
        self.player.health = self.player.max_health
        self.all_monsters.empty()
        self.comet_event.all_comets.empty()
        self.comet_event.reset_percent()

        # Ajuster la difficulté selon le niveau
        num_ogres = 2 + (level - 1)
        num_dragons = 1 + (level - 1) // 2  # 1 pour niv 1-2, 2 pour niv 3

        for _ in range(num_ogres):
            self.spawn_monster(Ogre)
        for _ in range(num_dragons):
            self.spawn_monster(Dragon)

    # Relancer une vague après l'événement comète
    def restart_wave(self):
        self.all_monsters.empty()
        num_ogres = 2 + (self.level - 1)
        num_dragons = 1 + (self.level - 1) // 2
        for _ in range(num_ogres):
            self.spawn_monster(Ogre)
        for _ in range(num_dragons):
            self.spawn_monster(Dragon)

    # Fin de la partie
    def game_over(self):
        # Sauvegarder le meilleur score si le score du joueuer est plus élevé que le prescedant
        if self.player.score > self.best_score:
            self.best_score = self.player.score
            with open(self.best_score_path, 'w') as f:
                f.write(str(self.best_score))
        self.all_monsters.empty()
        self.comet_event.all_comets.empty()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.is_game_over = True
        self.player.score = 0
        self.sound_manager.play("game_over")

    # Affichage écran de fin de partie
    def display_game_over(self, screen):
        screen.blit(self.game_over_image, (0, 0))
        title = self.go_title_font.render("Vous avez péri", True, RED)
        screen.blit(title, title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)))

        pygame.draw.rect(screen, (200, 200, 200), self.go_restart_button)
        restart_text = self.go_sub_font.render("Recommencer", True, BLACK)
        screen.blit(restart_text, restart_text.get_rect(center=self.go_restart_button.center))

        pygame.draw.rect(screen, (200, 200, 200), self.go_menu_button)
        menu_text = self.go_sub_font.render("Retour au menu", True, BLACK)
        screen.blit(menu_text, menu_text.get_rect(center=self.go_menu_button.center))

    # Mise à jour de la partie
    def update(self, screen):
        # Joueur et barre de vie
        screen.blit(self.player.image, self.player.rect)
        self.player.update_health_bar(screen)

        # Barre de progression comète
        self.comet_event.update_bar(screen)

        # Projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()
        self.player.all_projectiles.draw(screen)

        # Monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
        self.all_monsters.draw(screen)

        # Comètes
        for comet in self.comet_event.all_comets:
            comet.fall()
        self.comet_event.all_comets.draw(screen)

        # Déplacements joueur
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.right < SCREEN_WIDTH:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.left > 0:
            self.player.move_left()

    # Système de Collision
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    # Spawn des monstres
    def spawn_monster(self, monster_class_name=Ogre):
        self.all_monsters.add(monster_class_name(self))