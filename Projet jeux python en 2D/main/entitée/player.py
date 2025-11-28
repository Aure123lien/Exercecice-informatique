import pygame
from .projectile import Projectile
from ..configuration import *

# création de la classe du joueur, définir tous ses attributs
class Player(pygame.sprite.Sprite):

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
        pygame.draw.rect(surface, GRAY, [self.rect.x + 50, self.rect.y + 30, self.max_health, 5])
        pygame.draw.rect(surface, RED, [self.rect.x + 50, self.rect.y + 30, self.health, 5])

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
        self.game.sound_manager.play("tir")

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def add_score(self, points):
        self.score += points