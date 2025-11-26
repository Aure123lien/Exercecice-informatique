import pygame
from projectile import Projectile

# créer la classe Player
class Player(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 25
        self.velocity = 3
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("Projet jeux python en 2D/assets/Mage.png")

        # Redimensionner l'image du joueur
        self.image = pygame.transform.scale(self.image, (300, 250))
        
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 410

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            # si le personnage n'a plus de vie
            self.game.game_over()

    def update_health_bar(self, surface):
        # mettre la barre de vie visuellement
        pygame.draw.rect(surface, (94, 90, 90), [self.rect.x + 50, self.rect.y + 30, self.max_health, 5])
        pygame.draw.rect(surface, (255, 41, 0), [self.rect.x + 50, self.rect.y + 30, self.health, 5])

    def launch_projectile(self):
        # création de la classe projectile
        self.all_projectiles.add(Projectile(self))
        # jouer le son
        self.game.sound_manager.play("tir")

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
           self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
