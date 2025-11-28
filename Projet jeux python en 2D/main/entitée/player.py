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
        self.image = pygame.image.load(PLAYER_IMG_PATH)
        self.image = pygame.transform.scale(self.image, (300, 250))
        self.rect = self.image.get_rect()
        # Position initiale sur le sol
        self.rect.x = 350
        self.rect.y = SCREEN_HEIGHT - self.image.get_height() - 50

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.game_over()

    def update_health_bar(self, surface):
        bar_width = 100
        bar_height = 5
        bar_x = self.rect.centerx - bar_width // 2
        bar_y = self.rect.y - 30
        pygame.draw.rect(surface, GRAY, [bar_x, bar_y, bar_width, bar_height])
        pygame.draw.rect(surface, RED, [bar_x, bar_y, (self.health / self.max_health) * bar_width, bar_height])
        text = font.render(f"{int(self.health)}/{int(self.max_health)}", True, BLACK)
        text_rect = text.get_rect(centerx=self.rect.centerx, y=bar_y - 20)
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