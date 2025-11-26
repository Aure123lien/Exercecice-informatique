import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 25
        self.velocity = 3
        self.all_projectiles = pygame.sprite.Group()
        self.score = 0 
        self.image = pygame.image.load("Projet jeux python en 2D/assets/Mage.png")
        self.image = pygame.transform.scale(self.image, (300, 250))
        self.rect = self.image.get_rect()
        # Position initiale sur le sol
        self.rect.x = 350
        self.rect.y = 1080 - self.image.get_height() - 130

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.game_over()

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (94, 90, 90), [self.rect.x + 50, self.rect.y + 30, self.max_health, 5])
        pygame.draw.rect(surface, (255, 41, 0), [self.rect.x + 50, self.rect.y + 30, self.health, 5])

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







