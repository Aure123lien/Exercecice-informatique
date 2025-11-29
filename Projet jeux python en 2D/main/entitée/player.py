import pygame
from .projectile import Projectile
from ..configuration import *

font = pygame.font.SysFont("Arial", 16)

# création de la classe du joueur, définir tous ses attributs
class Player(pygame.sprite.Sprite):
    # Le joueur principal le mage tire des projectiles

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = PLAYER_MAX_HEALTH
        self.max_health = PLAYER_MAX_HEALTH
        self.attack = PLAYER_ATTACK
        self.velocity = PLAYER_VELOCITY
        self.all_projectiles = pygame.sprite.Group()
        self.score = 0
        self.level = 1
        self.xp = 0
        self.xp_to_next = 100
        self.image = pygame.image.load(PLAYER_IMG_PATH)
        self.image = pygame.transform.scale(self.image, (300, 250))
        self.rect = self.image.get_rect()
        # Position initiale sur le sol de la carte
        self.rect.x = 350
        self.rect.y = SCREEN_HEIGHT - self.image.get_height() - 50
        self.load_stats()

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.game_over()

    def update_health_bar(self, surface):
        bar_width = 100
        bar_height = 5
        bar_x = self.rect.centerx - bar_width // 2 - 20
        bar_y = self.rect.y - 10
        pygame.draw.rect(surface, GRAY, [bar_x, bar_y, bar_width, bar_height])
        pygame.draw.rect(surface, RED, [bar_x, bar_y, (self.health / self.max_health) * bar_width, bar_height])
        text = font.render(f"{int(self.health)}/{int(self.max_health)}", True, BLACK)
        text_rect = text.get_rect(centerx=self.rect.centerx - 20, y=bar_y - text.get_height())
        surface.blit(text, text_rect)

    def launch_projectile(self):
        # Créer un nouveau projectile et jouer le son
        self.all_projectiles.add(Projectile(self))
        self.game.sound_manager.play("tir")

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def add_score(self, points):
        self.score += points

    def add_xp(self, amount):
        self.xp += amount
        while self.xp >= self.xp_to_next:
            self.xp -= self.xp_to_next
            self.level_up()
        self.save_stats()

    def level_up(self):
        self.level += 1
        self.xp_to_next += 50  # Augmenter l'XP requis de 50 xp par niveau
        self.max_health += 10
        self.health = self.max_health 
        self.attack += 5
        self.velocity += 1
        # Peut-être jouer un son lorsqu'on passerait de niveaux ou afficher un message mais pour l'instant la fonctionnalité n'a rien

    def load_stats(self):
        try:
            with open('player_stats.txt', 'r') as f:
                lines = f.readlines()
                self.level = int(lines[0].strip())
                self.xp = int(lines[1].strip())
                self.xp_to_next = int(lines[2].strip())
                self.max_health = int(lines[3].strip())
                self.attack = int(lines[4].strip())
                self.velocity = int(lines[5].strip())
        except:
            pass  
        # Utiliser les valeurs par défaut

    def save_stats(self):
        with open('player_stats.txt', 'w') as f:
            f.write(f"{self.level}\n")
            f.write(f"{self.xp}\n")
            f.write(f"{self.xp_to_next}\n")
            f.write(f"{self.max_health}\n")
            f.write(f"{self.attack}\n")
            f.write(f"{self.velocity}\n")