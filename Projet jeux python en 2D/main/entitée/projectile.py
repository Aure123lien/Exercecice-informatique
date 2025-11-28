import pygame
from ..configuration import *

# Definir la classe pour configurer le projectile du personnage
class Projectile(pygame.sprite.Sprite):

     def __init__(self, player):
           super().__init__()
           self.velocity = PROJECTILE_VELOCITY 
           self.player = player
           self.image = pygame.image.load(PROJECTILE_IMG_PATH)

           # Réduction de la taille du projectile
           self.image = pygame.transform.scale(self.image, (70, 70))

           self.rect = self.image.get_rect()
           self.rect.x = player.rect.x + 300
           self.rect.y = player.rect.y + 80
           self.origin_image = self.image
           self.angle = 0

     def rotate(self):
           # faire tourner le projectile
           self.angle += 1
           self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
           self.rect = self.image.get_rect(center=self.rect.center)

     def remove(self):
           self.player.all_projectiles.remove(self)

     def move(self):
           self.rect.x += self.velocity
           self.rotate()

           # detection collision avec les monstres
           for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
                self.remove()
                monster.damage(self.player.attack)

           # retirer le projectile s'il sort de l'écran
           if self.rect.x > SCREEN_WIDTH:
               self.remove()